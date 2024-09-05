"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def __init__(self, pick) -> None:
        self.pick = pick

    def guess(self, n: int) -> int:
        """Returns whether the true number is higher or lower."""
        if n > self.pick:
            return -1
        elif n < self.pick:
            return 1
        else:
            return 0

    def guess_number(self, n: int) -> int:
        """
        Guesses at a number by calling to a LeetCode provided API, to then try
        to guess the correct number. Return the number when the API says we've
        gotten it correct.

        Args:
            `n`: The maximum number allowed in guesses.
        Returns:
            `number`: The found correct guess.
        """

        # Binary search towards the number.
        number = n
        space_left = n
        query = self.guess(number)
        while query != 0 and space_left > 0:
            query = self.guess(number)
            if query == -1:
                number -= space_left
            elif query == 1:
                number += space_left
            space_left = space_left // 2

        # If our binary search didn't quite bring us there. Step slowly.
        while query != 0:
            query = self.guess(number)
            if query == -1:
                number -= 1
            elif query == 1:
                number += 1
        return number
