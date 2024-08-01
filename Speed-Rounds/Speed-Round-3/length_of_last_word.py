class Solution:
    """Problem provided by LeetCode"""

    def length_of_last_word(self, s: str) -> int:
        """
        Returns the length of the last word in a string of words separated by
        spaces. Could have trailing spaces.

        Args:
            `s`: The full string with spaces.
        Returns:
            `count`: The number of characters of the last word in the string.
        """

        # 5 min

        # Count letters from the end until we find a space.
        # Start counting once we hit a letter.
        count = 0
        has_found_word = False
        for i in range(len(s) - 1, -1, -1):
            if has_found_word:
                if s[i] == " ":
                    return count
                count += 1
            elif s[i] != " ":
                has_found_word = True
                count += 1
        return count
