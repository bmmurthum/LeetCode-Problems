""" 
The methods of this class return a string that represent the words 
being flipped in order. 
"""


class Solution:
    """Given class by LeetCode to perform methods in"""

    # My solution
    def reversewords_1(self, s: str) -> str:
        """
        Returns a string of the input string's `s` words in reverse order.
        """
        s = s.strip()
        while "  " in s:
            s = s.replace("    ", "  ")
            s = s.replace("  ", " ")
        words = s.split(" ")
        words.reverse()
        s = words[0]
        for w in range(1, len(words)):
            s = s + " " + words[w]
        return s

    # My solution without double-replace.
    def reversewords_2(self, s: str) -> str:
        """
        Returns a string of the input string's `s` words in reverse order.
        """
        s = s.strip()
        while "  " in s:
            s = s.replace("  ", " ")
        words = s.split(" ")
        words.reverse()
        s = words[0]
        for w in range(1, len(words)):
            s = s + " " + words[w]
        return s

    # My solution without double-replace, without list-reverse
    def reversewords_3(self, s: str) -> str:
        """
        Returns a string of the input string's `s` words in reverse order.
        """
        s = s.strip()
        while "  " in s:
            s = s.replace("  ", " ")
        words = s.split(" ")
        s = words[len(words) - 1]
        for w in range(len(words) - 2, -1, -1):
            s = s + " " + words[w]
        return s

    # Someone else's solution
    def reversewords_4(self, s: str) -> str:
        """
        Returns a string of the input string's `s` words in reverse order.
        """
        words = s.split()
        words.reverse()
        return " ".join(words)

    # Someone else's solution
    def reversewords_5(self, s: str) -> str:
        """
        Returns a string of the input string's `s` words in reverse order.
        """
        r = s.strip().split(" ")
        r1 = r[::-1]
        r2 = [i for i in r1 if i != ""]
        s2 = " ".join(r2)
        return s2
