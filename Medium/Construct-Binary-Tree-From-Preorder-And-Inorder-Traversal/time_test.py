"""Module for testing function time performance"""

import timeit

# from construct_binary_tree_from_preorder import Solution
# from other_solution import Solution as Solution2

NUM_TESTS = 2000


# My solution
MYSETUP = """
from construct_binary_tree_from_preorder import Solution
from test_cases import TestCases
"""
MYCODE = """
s = Solution()
result_1 = s.build_tree_1(TestCases.test_2[0],TestCases.test_2[1])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("build_tree_1 Running Time: " + TIME_PER_RUN)


# Someone else's solution
MYSETUP = """
from other_solution import Solution as Solution2
from test_cases import TestCases
"""
MYCODE = """
s = Solution2()
result_1 = s.build_tree_2(TestCases.test_2[0],TestCases.test_2[1])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("build_tree_2 Running Time: " + TIME_PER_RUN)
