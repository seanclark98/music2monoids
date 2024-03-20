from copy import deepcopy

from .chords import Chord, all_chords


class ParsimoniousRelation:
    def __init__(
        self,
        chord_length: int,
        from_chord_type: tuple[int, ...],
        to_chord_type: tuple[int, ...],
        root_shift: int,
    ):
        self.chord_length = chord_length
        self.from_chord_type = from_chord_type
        self.to_chord_type = to_chord_type
        self.root_shift = root_shift

    def __call__(self, chord: Chord) -> Chord | None:
        if not self.is_parsimonious():
            return None

        chord_type = chord.intervals
        match chord_type:
            case self.from_chord_type:
                new_root = (chord.root + self.root_shift) % 12
                new_chord = Chord(*self.to_chord_type) + new_root
            case self.to_chord_type:
                new_root = (chord.root - self.root_shift) % 12
                new_chord = Chord(*self.from_chord_type) + new_root
            case _:
                new_chord = deepcopy(chord)

        return new_chord

    def is_parsimonious(self) -> bool:
        from_chord = Chord(*self.from_chord_type)
        to_chord = Chord(*self.to_chord_type) + self.root_shift
        return from_chord.parsimonious(to_chord)

    def as_permutation(self) -> tuple[int, ...] | None:
        if not self.is_parsimonious():
            return None

        permutation = list(range(1, len(all_chords(self.chord_length)) + 1))

        for root in range(12):
            from_chord = Chord(*self.from_chord_type) + root
            permutation[from_chord.index] = self(from_chord).index + 1

            to_chord = Chord(*self.to_chord_type) + root
            permutation[to_chord.index] = self(to_chord).index + 1
        return tuple(permutation)
