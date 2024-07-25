""" Module to tell if a number is a "happy number." """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    known_false_set = {
        2,
        3,
        4,
        5,
        6,
        8,
        9,
        11,
        12,
        14,
        15,
        16,
        17,
        18,
        20,
        25,
        26,
        27,
        29,
        34,
        36,
        37,
        40,
        41,
        42,
        46,
        50,
        52,
        53,
        54,
        58,
        61,
        64,
        65,
        81,
        85,
        89,
        113,
        145,
    }

    def is_happy(self, n: int) -> bool:
        """
        Tells us if an integer is a "happy number."

        Args:
            `n`: Number to look at
        Returns:
            `True/False`: If number is happy.
        """

        past_numbers = set()

        while True:
            if n == 1:
                return True
            elif n in past_numbers:
                return False
            else:
                past_numbers.add(n)
                temp = str(n)
                total = 0
                for digit in temp:
                    total += (int(digit)) ** 2
                n = total

    def is_happy_b(self, n: int) -> bool:
        """
        Tells us if an integer is a "happy number."

        Args:
            `n`: Number to look at
        Returns:
            `True/False`: If number is happy.
        """

        past_numbers = set()

        while True:
            if n == 1:
                return True
            elif n in past_numbers or n in self.known_false_set:
                return False
            else:
                past_numbers.add(n)
                temp = str(n)
                total = 0
                for digit in temp:
                    total += (int(digit)) ** 2
                n = total
