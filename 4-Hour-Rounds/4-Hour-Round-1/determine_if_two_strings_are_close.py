"""Problem from LeetCode.com"""

# Ignore the advice to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def close_strings(self, word1: str, word2: str) -> bool:
        """
        Through two offered operations, can these two words be turned into one
        another? (1) Swapping letter placements within a word. (2) Swapping all
        of one letter in a word with another letter.

        Args:
            `word1`: Our first word.
            `word2`: A goal word.
        Returns:
            `True/False`: Whether we can change one word to the other with
                allowed operations.
        """

        # Handle edge-cases.
        # - Are the words the same length?
        if len(word1) != len(word2):
            return False

        # Setup
        word1_dict = {}
        word1_set = set(word1)
        word2_dict = {}
        word2_set = set(word2)

        # Does each word have the same amount of unique letters?
        if len(word1_set) != len(word2_set):
            return False

        # Is each letter shared between both?
        for word in word1_set:
            if word not in word2_set:
                return False

        # Figure counts of each unique letter.
        for letter in word1_set:
            word1_dict[letter] = 0
        for letter in word2_set:
            word2_dict[letter] = 0
        for letter in word1:
            word1_dict[letter] += 1
        for letter in word2:
            word2_dict[letter] += 1

        # Build two lists of counts of unique letters.
        word1_values = list(word1_dict.values())
        word2_values = list(word2_dict.values())
        word1_values.sort()
        word2_values.sort()

        # If the counts of unique letters match, we know we can transform to
        # the other word.
        if word1_values == word2_values:
            return True
        else:
            return False
