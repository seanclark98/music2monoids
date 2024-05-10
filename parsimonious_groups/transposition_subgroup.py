"""
R - group of transposing transformations (transposing in the musical sense)
Those transformations that shift the root of a chord, but do not change it's type.
Such transformations can be represented as Z_12^t,
where t=no_of_types(n) and n is the chord length.
"""

from sage.all_cmdline import gap


def perm_and_tuple_to_transformation(
    perm: list[int], tup: list[int], n_types: int
) -> gap.Transformation:
    """
    perm: permutation on chords types
    tup: root shift tuple - chord of type t is transposed by tup[t]
    """
    n_chords = 12 * n_types
    trans = [0] * n_chords

    for chord_type in range(0, n_types):
        for root in range(0, 12):
            transpose = tup[chord_type]
            trans[chord_type + root * n_types] = (
                perm[chord_type] + root * n_types + transpose * n_types
            ) % n_chords

    return gap.Transformation([x + 1 for x in trans])


def phi(tup: list, n_types: int) -> gap.Transformation:
    identity_permutation = list(range(n_types))
    return perm_and_tuple_to_transformation(identity_permutation, tup, n_types)


def standard_generators_for_direct_product_of_cyclic_groups(n: int) -> list[list[int]]:
    return [[0] * i + [1] + [0] * (n - i - 1) for i in range(n)]


def subset_of_direct_product_of_cyclic_groups(n: int) -> list[list[int]]:
    return [
        gen + [-1]
        for gen in standard_generators_for_direct_product_of_cyclic_groups(n - 1)
    ]


def possible_gens_for_R(n_types: int) -> list[gap.Transformation]:
    """Q in paper."""
    return [
        phi(gen, n_types) for gen in subset_of_direct_product_of_cyclic_groups(n_types)
    ]


def c12_pow(n: int) -> str:
    return " x ".join(["C12"] * n)


def is_isomorphic_to_c12_direct_product(group: gap.Group, k: int) -> bool:
    """
    k: number of direct products of C12
    """
    return str(gap.StructureDescription(group)) == c12_pow(k)
