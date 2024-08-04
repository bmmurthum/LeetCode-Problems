class Solution:
    """Problem provided by LeetCode"""

    def max_vowels(self, s: str, k: int) -> int:
        """
        Count the maximum number of vowels in a given sized window on a string.

        Args:
            `s`: The given string.
            `k`: The search window size.
        Returns:
            `max_num`: The maximum number of vowels in one chunk.
        """

        # 9 min

        # Fixes:
        # - Time limit exceeded. Had to explore new pattern without substring
        #   counting.

        vowels = {"a", "e", "i", "o", "u"}

        # Handle edge-cases
        if k == 1:
            for letter in vowels:
                if letter in s:
                    return 1
            return 0
        if len(s) == 1:
            if s[0] in vowels:
                return 1
            else:
                return 0

        # Count vowels in first substring.
        count = 0
        for char in s[0:k]:
            if char in vowels:
                count += 1

        # Go through the string with a sliding window and keep a maximum count
        # of vowels found in any substring. Break early if max matches k.
        max_num = count
        for i in range(1, len(s) - k + 1):
            # Add the new char
            if s[i + k - 1] in vowels:
                count += 1
            # Remove the old char
            if s[i - 1] in vowels:
                count -= 1
            # Is this a new max?
            if count > max_num:
                max_num = count
        return max_num
