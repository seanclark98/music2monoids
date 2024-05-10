from sage.all_cmdline import gap

from permutations.chords import no_of_types
from permutations.permutations import all_permutations


def is_transposition_in_gens(
    a: int, b: int, n_types: int, gens: list[gap.Transformation]
) -> bool:
    # TODO: rewrite with a and b being instances of `Chord` instead of integers
    src = []
    dst = []

    n_chords = 12 * n_types
    while a <= n_chords:
        src.append(a)
        dst.append(b)

        src.append(b)
        dst.append(a)

        a = a + n_types
        b = ((b + n_types - 1) % n_chords) + 1
    return gap.TransformationListList(src, dst) in gens


# A transposition is a permutation which interchanges two elements and leaves
# everything else fixed.
# finds all parallel transformations in Gens (P \cap \mathcal{T}_l)
def all_transpositions_in_gens(
    n: int, gens: list[gap.Transformation]
) -> list[gap.Transformation]:
    transpositions = []
    n_types = no_of_types(n)

    for i in range(1, n_types + 1):
        for j in range(1, n_types + 1):
            if j == i:
                continue
            if is_transposition_in_gens(i, j, n_types, gens):
                transpositions.append(gap.Transformation([i, j], [j, i]))
    return transpositions


def transformation_semigroup_on_all_tertian_n_chords(n: int) -> gap.Semigroup:
    """Generates the transformation semigroup on the set of all tertian
    n-chords."""
    return gap.Semigroup(all_permutations(n))


def transformation_group_on_all_tertian_n_chords(n: int) -> gap.Group:
    """Generates the transformation group on the set of all tertian
    n-chords."""
    return gap.Group(all_permutations(n))


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


"""
R - group of transposing transformations (transposing in the musical sense)
Those transformations that shift the root of a chord, but do not change it's type.
Such transformations can be represented as Z_12^t,
where t=no_of_types(n) and n is the chord length.
"""


if __name__ == "__main__":
    for n in range(2, 12):  # n = chord_length
        print(f"Transformation Semigroup on the set of all tertian {n}-chords")
        G = transformation_group_on_all_tertian_n_chords(n)
        t = no_of_types(n)

        # Prove that C12^(t-1) is isomorphic to R
        Q = possible_gens_for_R(t)
        assert gap.IsSubset(G, Q)  # check
        group_generated_by_Q = gap.Group(Q)
        assert is_isomorphic_to_c12_direct_product(group_generated_by_Q, t - 1)
        assert gap.Size(group_generated_by_Q) == 12 ** (t - 1)
        # => group_generated_by_Q is isomorphic to R
        # => C12^(t-1) is isomorphic to R

        print("\n")
