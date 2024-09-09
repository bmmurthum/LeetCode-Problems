"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def num_tilings(self, n: int) -> int:
        """
        We're asked to look at two shaped dominos, one with an I shape and one
        with an L shape. How many different ways can you place these pieces
        neatly into a given space with height of 2 and width of `n`?

        t0 = 0, t1 = 1, t2 = 2, t3 = 5, t4 = 11, tn = (2 * (tn-1)) + tn-3

        Args:
            `n`: The width of the given space to keep our shapes in.
        Returns:
            `output`: The number of different positions the shapes can be in.
        """

        # We solved this by drawing our the shapes for a handful of initial
        # cases to see there was some pattern in the numbers. It looks like
        # there's something similar to a fibonacci pattern, so we found a
        # pattern.

        # Because the answers become so large, it was asked to return the
        # answer with a given modulus of `modulus`.

        # Edge-case: The interested value is first-defined.
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        # Run a dynamic-programming method to generate the new numbers upward.
        a = 1
        b = 2
        c = 5
        modulus = (10**9) + 7
        for _ in range(3, n):
            temp = (c * 2) + a
            a = b
            b = c
            c = temp
        return c % modulus
