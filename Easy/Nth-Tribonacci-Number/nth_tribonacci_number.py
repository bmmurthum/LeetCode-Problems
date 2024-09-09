"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def tribonacci(self, n: int) -> int:
        """
        Finds the nth number in a tribonacci sequence.

        t0 = 0, t1 = 1, t2 = 1, tn = tn-1 + tn-2 + tn-3

        Args:
            `n`: The index of the number we're interested in.
        Returns:
            `output`: The value of this number.
        """

        # Edge-case: target is defined in definition.
        if n == 0:
            return 0
        if n in {1, 2}:
            return 1

        # Build a list of the solutions that lead up to our answer, calling
        # back on previous answers to build to the next. We could have this
        # `found` list as a queue with a push() pop() strategy, but our list is
        # guaranteed to be at most 37 values and feels unnecessary. The adding
        # and removing values from front and back of the list may be costly in
        # processing.

        # LeetCode submissions use this preceding strategy and end up being
        # 30% faster.

        found = [0, 1, 1]
        i = 3
        while i <= n:
            new = found[i - 1] + found[i - 2] + found[i - 3]
            found.append(new)
            i += 1
        return found[-1]
