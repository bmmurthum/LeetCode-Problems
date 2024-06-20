"""Module for testing function time performance"""

import timeit


NUM_TESTS = 2000


# My solution
MYSETUP = """
from maximum_depth_of_binary_tree import Solution
from test_cases import TestCases
"""
MYCODE = """
s = Solution()
result_1 = s.max_depth_1(TestCases.test_1_head)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("max_depth_1 Running Time: " + TIME_PER_RUN)


# My solution, without storing internal results to variables
MYSETUP = """
from maximum_depth_of_binary_tree_2 import Solution as Solution2
from test_cases import TestCases
"""
MYCODE = """
t = Solution2()
result_2 = t.max_depth_2(TestCases.test_1_head)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("max_depth_2 Running Time: " + TIME_PER_RUN)
