class Solution:
    """Problem provided by LeetCode"""

    def merge_alternately_initial(self, word1: str, word2: str) -> str:
        """
        Returns a string that is a merged version of the two input strings. One
        letter from each word is added to a new string alternately. If one
        string is longer, the ending piece of that string is added to the end.

        Ex: word1 == "abc", word2 == "defgh", new_string == "adbecfgh"

        Args:
            `word1`: First string.
            `word2`: Second string.
        Returns:
            `new_string`: The newly merged string.
        """

        # 9 min, 40 sec.

        # Thought about using zip for a moment. I'm unsure how it works with
        # differing sized strings.

        new_string = ""
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            new_string += word1[i]
            new_string += word2[i]
        if len(word1) > min_length:
            new_string += word1[min_length:]
        elif len(word2) > min_length:
            new_string += word2[min_length:]

        return new_string
