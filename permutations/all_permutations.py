from itertools import product

from .chords import all_chord_types
from .parsimonious_relation import ParsimoniousRelation


def all_permutations(length: int) -> set[tuple[int, ...]]:
    permutations = set()

    for from_chord_type, to_chord_type in product(all_chord_types(length), repeat=2):
        for root_shift in range(12):
            relation = ParsimoniousRelation(
                length, from_chord_type.intervals, to_chord_type.intervals, root_shift
            )
            permutation = relation.as_permutation()
            if permutation is not None and permutation not in permutations:
                permutations.add(permutation)
    return permutations
