class Solution:
    """Problem provided by LeetCode"""

    def longest_common_prefix(self, strs: list[str]) -> str:
        """
        Returns the shared first common letters between a list of strings.

        Args:
            `strs`: A list of strings to look at.
        Returns:
            `longest_chunk`: The longest string of beginning characters.
        """

        # 6 min

        # Fixes:
        # - +1 fix on the range()
        # - Checking that `curr_chunk` is equal to a similar `item` substring,
        #   instead of that its "in" the string.

        # Create a set of the strings
        # Find the shortest string of the list
        str_set = set(strs)
        shortest = strs[0]
        for item in str_set:
            if len(item) < len(shortest):
                shortest = item

        # Look for a growing length chunk of letters in each string
        longest_chunk = ""
        for i in range(1, len(shortest) + 1):
            curr_chunk = shortest[:i]
            for item in str_set:
                if curr_chunk != item[:i]:
                    return longest_chunk
            longest_chunk = curr_chunk
        return longest_chunk
