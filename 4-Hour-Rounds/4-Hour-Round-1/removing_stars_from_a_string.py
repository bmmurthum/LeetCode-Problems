"""Problem from LeetCode.com"""

# Ignore the advice to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def remove_stars(self, s: str) -> str:
        """
        Return a transformed string that has any letters to the left of an
        asterisk removed along with those asterisks.

        Args:
            `s`: The given string.
        Returns:
            `new_string`: The transformed string.
        """

        # Build a stack and pop when meeting an asterisk.
        our_stack = []
        for letter in s:
            if letter != "*":
                our_stack.append(letter)
            else:
                our_stack.pop()

        # Build string from stack
        new_string = ""
        for letter in our_stack:
            new_string += letter
        return new_string
