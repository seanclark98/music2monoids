from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def all_chord_types(length: int) -> list["Chord"]:
    if length == 1:
        return [Chord(0)]
    chords = []
    for chord in all_chord_types(length - 1):
        for interval in [3, 4]:
            if (note := (chord[-1] + interval) % 12) not in chord:
                chords.append(Chord(*chord.pitch_classes, note))
    return chords


@lru_cache(maxsize=None)
def all_chords(length: int) -> list["Chord"]:
    chord_types = all_chord_types(length)
    return [chord_type + i for i in range(12) for chord_type in chord_types]


@lru_cache(maxsize=None)
def chord_to_index(chord: "Chord") -> int:
    length = len(chord)
    return all_chords(length).index(chord)


@lru_cache(maxsize=None)
def index_to_chord(index: int, length: int) -> "Chord":
    return all_chords(length)[index]


@lru_cache(maxsize=None)
def no_of_types(length: int) -> int:
    return int(len(all_chord_types(length)))


@lru_cache(maxsize=None)
def index_to_chord_type_index(index: int, length: int) -> int:
    return index % no_of_types(length)


@lru_cache(maxsize=None)
def index_to_root(index: int, length: int) -> int:
    return index // no_of_types(length)


def root_and_type_to_index(root: int, chord_type_index: int, length: int) -> int:
    return int(
        (root * no_of_types(length) + chord_type_index) % len(all_chords(length))
    )


class Chord:
    def __init__(self, *pitch_classes: int):
        self.pitch_classes = tuple([pitch_class % 12 for pitch_class in pitch_classes])
        self.root = self.pitch_classes[0]
        self.intervals = tuple(
            [(pitch_class - self.root) % 12 for pitch_class in self.pitch_classes]
        )

    def __repr__(self) -> str:
        return str(self.pitch_classes)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Chord):
            return False
        return self.pitch_classes == other.pitch_classes

    def __len__(self) -> int:
        return len(self.pitch_classes)

    def __hash__(self) -> int:
        return hash(self.pitch_classes)

    def __getitem__(self, key: int) -> int:
        return self.pitch_classes[key]

    def __setitem__(self, key: int, value: int) -> None:
        intervals = list(self.pitch_classes)
        intervals[key] = value
        self.pitch_classes = tuple(intervals)

    def __add__(self, interval: int) -> "Chord":
        """Transpose chord by interval."""
        return Chord(*[pitch_class + interval for pitch_class in self.pitch_classes])

    def __contains__(self, item: object) -> bool:
        return item in self.pitch_classes

    def equivalent(self, other: "Chord") -> bool:
        return set(self.pitch_classes) == set(other.pitch_classes)

    def parsimonious(self, other: "Chord") -> bool:
        if len(self) != len(other):
            return False

        X = Counter(self.pitch_classes)
        Y = Counter(other.pitch_classes)
        diff1 = X - Y
        diff2 = Y - X

        if not (len(diff1) == len(diff2) == 1):
            return False
        [(k1, v1)] = diff1.items()
        [(k2, v2)] = diff2.items()
        if v1 == 1 and v2 == 1 and (k1 - k2) % 12 in [1, 11]:
            return True
        return False

    @property
    def index(self) -> int:
        return chord_to_index(self)
