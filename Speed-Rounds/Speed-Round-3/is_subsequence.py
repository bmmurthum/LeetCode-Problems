class Solution:
    """Problem provided by LeetCode"""

    def is_subsequence(self, s: str, t: str) -> bool:
        """
        Tells us if the subsequence is inside the longer string.

        Args:
            `s`: The subsequence to search for.
            `t`: The longer string.
        Returns:
            `True/False`: Whether it was found.
        """

        # 7 min

        # Fixes:
        # - Had to explore new pattern
        # - Little things in wrong order

        # Handle edge cases
        if s == "":
            return True
        elif t == "":
            return False

        # Look for each letter in order
        s_found_count = 0
        s_length = len(s)
        t_index = 0
        t_length = len(t)
        for letter in s:
            while t_index < t_length:
                if t[t_index] == letter:
                    t_index += 1
                    s_found_count += 1
                    break
                t_index += 1
            if s_found_count == s_length:
                return True
            if t_index == t_length:
                return False
