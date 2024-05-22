from itertools import product

from sage.all_cmdline import gap

from .chords import all_chord_types
from .parsimonious_relation import ParsimoniousRelation


def all_transformations(length: int) -> list[gap.Transformation]:
    """All parsimonious transformations (as transformations) on the set of all
    n-chords."""
    transformations = set()

    for from_chord_type, to_chord_type in product(all_chord_types(length), repeat=2):
        for root_shift in range(12):
            relation = ParsimoniousRelation(
                length, from_chord_type.intervals, to_chord_type.intervals, root_shift
            )
            transformation = relation.as_transformation()
            if transformation is not None and transformation not in transformations:
                transformations.add(transformation)
    return [gap.Transformation(perm) for perm in transformations]


def transformation_semigroup_on_all_tertian_n_chords(n: int) -> gap.Semigroup:
    """Generates the transformation semigroup on the set of all tertian
    n-chords."""
    return gap.Semigroup(all_transformations(n))


def transformation_group_on_all_tertian_n_chords(n: int) -> gap.Group:
    """Generates the transformation group on the set of all tertian
    n-chords."""
    return gap.Group(all_transformations(n))
