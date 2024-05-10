from sage.all_cmdline import gap

from .chords import no_of_types
from .parsimonious_group import transformation_group_on_all_tertian_n_chords
from .transposition_subgroup import (
    is_isomorphic_to_c12_direct_product,
    possible_gens_for_R,
)

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
