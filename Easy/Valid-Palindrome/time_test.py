"""Module for testing function time performance"""

import timeit

NUM_TESTS = 500

# My solution
MYSETUP = """
class Solution:
    def is_palindrome_1(self, s: str) -> bool:
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
"""
MYCODE = """
sol = Solution()
S = "123456788889888888754321"
RESULT = sol.is_palindrome_1(S)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("is_palindrome_1():" + TIME_PER_RUN)


# Someone else's solution
MYSETUP = """
class Solution:
    def is_palindrome_2(self, s: str) -> bool:
        str1 = "".join([i for i in s if i.isalnum()]).lower()
        if str1 == str1[::-1]:
            return True
        else:
            return False
"""
MYCODE = """
sol = Solution()
S = "123456788889888888754321"
RESULT = sol.is_palindrome_2(S)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("is_palindrome_2():" + TIME_PER_RUN)


# Someone else's solution
MYSETUP = """
import re
class Solution:
    def is_palindrome_3(self, s: str) -> bool:
        cleaned = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        left, right = 0, len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
"""
MYCODE = """
sol = Solution()
S = "123456788889888888754321"
RESULT = sol.is_palindrome_3(S)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("is_palindrome_3():" + TIME_PER_RUN)
