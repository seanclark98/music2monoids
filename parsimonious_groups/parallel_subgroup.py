from sage.all_cmdline import gap

from .chords import no_of_types, root_and_type_to_index


# Note: Transposition here refers to mathematical permutation transpositions
# this is confusing when also referring to musical transpositions
# TODO: Update terms to avoid confusion
def is_transposition_in_gens(
    type_a: int, type_b: int, n_types: int, gens: list[gap.Transformation]
) -> bool:
    # TODO: rewrite with a and b being instances of `Chord` instead of integers
    src = []
    dst = []

    for i in range(12):
        a = root_and_type_to_index(i, type_a - 1, n_types) + 1
        b = root_and_type_to_index(i, type_b - 1, n_types) + 1

        src.append(a)
        dst.append(b)

        src.append(b)
        dst.append(a)

    return gap.TransformationListList(src, dst) in gens


# A transposition is a permutation which interchanges two elements and leaves
# everything else fixed.
# finds all parallel transformations in Gens (P \cap \mathcal{T}_l)
def all_transpositions_in_gens(
    n: int, gens: list[gap.Transformation]
) -> list[gap.Transformation]:
    transpositions = []
    n_types = no_of_types(n)

    for type_a in range(1, n_types + 1):
        for type_b in range(1, n_types + 1):
            if type_b == type_a:
                continue
            if is_transposition_in_gens(type_a, type_b, n_types, gens):
                transpositions.append(
                    gap.Transformation([type_a, type_b], [type_b, type_a])
                )
    return transpositions
