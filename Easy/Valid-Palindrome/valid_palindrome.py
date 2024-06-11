""" A class with `is_palindrome_1(str)` to return `true` if the given string is a palindrome."""

# import re


class Solution:
    """LeetCode's object"""

    def is_palindrome_1(self, s: str) -> bool:
        """returns `True` if `s` is a palindrome"""
        r = len(s) - 1
        l = 0
        while r - l > 0:
            if s[r].isalnum() is False:
                r -= 1
                continue
            elif s[l].isalnum() is False:
                l += 1
                continue
            elif s[r].lower() == s[l].lower():
                r -= 1
                l += 1
            else:
                return False
        return True

    # # Someone elses's solution
    # def is_palindrome_2(self, s: str) -> bool:
    #     """returns `True` if `s` is a palindrome"""
    #     str1 = "".join([i for i in s if i.isalnum()]).lower()
    #     if str1 == str1[::-1]:
    #         return True
    #     else:
    #         return False

    # # Someone elses's solution
    # def is_palindrome_3(self, s: str) -> bool:
    #     """returns `True` if `s` is a palindrome"""
    #     cleaned = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    #     left, right = 0, len(cleaned) - 1

    #     while left < right:
    #         if cleaned[left] != cleaned[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True
