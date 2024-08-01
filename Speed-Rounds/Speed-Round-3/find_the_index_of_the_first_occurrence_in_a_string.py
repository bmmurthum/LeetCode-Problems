class Solution:
    """Problem provided by LeetCode"""

    def str_str(self, haystack: str, needle: str) -> int:
        """
        Is this continuous string found inside the longer string?

        Args:
            `haystack`: The longer string to search.
            `needle`: The string to be looking for.
        Returns:
            `i`: The index of the string. `-1` if not found.
        """

        # 6 min

        # Looking at each letter of the longer word, do the next 4* letters
        # spell out the small word we're looking for?
        size = len(needle)
        for i, letter in enumerate(haystack):
            if letter == needle[0] and haystack[i : i + size] == needle:
                return i
        return -1
