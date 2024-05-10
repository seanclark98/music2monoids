from itertools import product

from sage.all_cmdline import gap

from .chords import all_chord_types
from .parsimonious_relation import ParsimoniousRelation


def all_permutations(length: int) -> list[gap.Transformation]:
    """All parsimonious transformations (as permutations) on the set of all
    n-chords."""
    permutations = set()

    for from_chord_type, to_chord_type in product(all_chord_types(length), repeat=2):
        for root_shift in range(12):
            relation = ParsimoniousRelation(
                length, from_chord_type.intervals, to_chord_type.intervals, root_shift
            )
            permutation = relation.as_permutation()
            if permutation is not None and permutation not in permutations:
                permutations.add(permutation)
    return [gap.Transformation(perm) for perm in permutations]


def transformation_semigroup_on_all_tertian_n_chords(n: int) -> gap.Semigroup:
    """Generates the transformation semigroup on the set of all tertian
    n-chords."""
    return gap.Semigroup(all_permutations(n))


def transformation_group_on_all_tertian_n_chords(n: int) -> gap.Group:
    """Generates the transformation group on the set of all tertian
    n-chords."""
    return gap.Group(all_permutations(n))
