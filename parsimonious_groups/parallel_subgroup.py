from sage.all_cmdline import gap

from .chords import no_of_types


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
