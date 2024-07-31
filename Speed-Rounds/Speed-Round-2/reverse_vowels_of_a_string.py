class Solution:
    """Problem provided by LeetCode"""

    def reverse_vowels(self, s: str) -> str:
        """
        Reverses the vowels in a given string. Handled in-place.

        Args:
            `s`: The given string
        Returns:
            `s`: With changes.
        """

        # 5 min 30 sec

        # Had to fix to allow for capital vowels to be handled.
        # Had to fix an issue with trying to change a string's character.

        # Extract vowels
        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        our_vowel_list = []
        for _, letter in enumerate(s):
            if letter in vowel_set:
                our_vowel_list.append(letter)

        # Put them back in reversed
        temp_s = list(s)
        for i, letter in enumerate(s):
            if temp_s[i] in vowel_set:
                temp_s[i] = our_vowel_list.pop()
        s = "".join(temp_s)

        return s
