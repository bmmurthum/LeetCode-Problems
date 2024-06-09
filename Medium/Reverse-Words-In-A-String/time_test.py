"""Module for testing function time performance"""

import timeit

NUM_TESTS = 100

# My solution
MYCODE = """
class Solution:
    def reverseWords_1(self, s: str) -> str:
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
sol = Solution()
s = "     the   sky       is  blue     "
result = sol.reverseWords_1(s)
"""
TIME_PER_RUN = str(timeit.timeit(stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS)
print("reverseWords_1():" + TIME_PER_RUN)


MYCODE = """
class Solution:
    def reverseWords_2(self, s: str) -> str:
        s = s.strip()
        while "  " in s:
            s = s.replace("  ", " ")
        words = s.split(" ")
        words.reverse()
        s = words[0]
        for w in range(1, len(words)):
            s = s + " " + words[w]
        return s
sol = Solution()
s = "     the   sky       is  blue     "
result = sol.reverseWords_2(s)
"""
TIME_PER_RUN = str(timeit.timeit(stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS)
print("reverseWords_2():" + TIME_PER_RUN)


MYCODE = """
class Solution:
    def reverseWords_3(self, s: str) -> str:
        s = s.strip()
        while "  " in s:
            s = s.replace("  ", " ")
        words = s.split(" ")
        s = words[len(words) - 1]
        for w in range(len(words) - 2, -1, -1):
            s = s + " " + words[w]
        return s
sol = Solution()
s = "     the   sky       is  blue     "
result = sol.reverseWords_3(s)
"""
TIME_PER_RUN = str(timeit.timeit(stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS)
print("reverseWords_3():" + TIME_PER_RUN)


MYCODE = """
class Solution:
    def reverseWords_4(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)
sol = Solution()
s = "     the   sky       is  blue     "
result = sol.reverseWords_4(s)
"""
TIME_PER_RUN = str(timeit.timeit(stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS)
print("reverseWords_4():" + TIME_PER_RUN)


MYCODE = """
class Solution:
    def reverseWords_5(self, s: str) -> str:
        r = s.strip().split(" ")
        r1 = r[::-1]
        r2 = [i for i in r1 if i != ""]
        s2 = " ".join(r2)
        return s2
sol = Solution()
s = "     the   sky       is  blue     "
result = sol.reverseWords_5(s)
"""
TIME_PER_RUN = str(timeit.timeit(stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS)
print("reverseWords_5():" + TIME_PER_RUN)
