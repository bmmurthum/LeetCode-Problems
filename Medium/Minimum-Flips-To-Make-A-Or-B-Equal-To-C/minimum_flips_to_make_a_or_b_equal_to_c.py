"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def min_flips(self, a: int, b: int, c: int) -> int:
        """
        Given two numbers A and B, find the total number of bit flips between
        the two of them such that A bitwise-OR B equals C.

        Args:
            `a`: First number.
            `b`: Second number.
            `c`: The final number.
        Returns:
            `total_flips`: The a number of bit flips.
        """

        # For each bit, starting with 1, then 2, then 4, we're looking to see
        # if C has that bit as a 1 or 0, then looking at A and B to see what
        # changes need to be done and add those to a total as we iterate.

        max_num = max([a, b, c])
        check = 1
        total_flips = 0
        while check <= max_num:
            # Is C a 1 or 0?
            inside_c = (check & c) // check
            # If C at this bit == 1
            if inside_c == 1:
                a_b_total = ((check & a) + (check & b)) // check
                if a_b_total == 0:
                    total_flips += 1
            # If C at this bit == 0
            else:
                a_b_total = ((check & a) + (check & b)) // check
                total_flips += a_b_total
            # Next bit
            check *= 2
        return total_flips
