"""Module for testing function time performance"""

import timeit

NUM_TESTS = 2000


# Another person's solution
MYSETUP = """
from path_sum_3 import Solution
from test_cases import TestCases
"""
MYCODE = """
s = Solution()
result_3 = s.has_path_sum_3(TestCases.test_3[0],TestCases.test_3[1])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("has_path_sum_3() Running Time: " + TIME_PER_RUN)

# My solution
MYSETUP = """
from path_sum import Solution
from test_cases import TestCases
"""
MYCODE = """
s = Solution()
result_1 = s.has_path_sum_1(TestCases.test_3[0],TestCases.test_3[1])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("has_path_sum_1() Running Time: " + TIME_PER_RUN)


# Another person's solution
MYSETUP = """
from path_sum_2 import Solution
from test_cases import TestCases
"""
MYCODE = """
s = Solution()
result_2 = s.has_path_sum_2(TestCases.test_3[0],TestCases.test_3[1])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("has_path_sum_2() Running Time: " + TIME_PER_RUN)
