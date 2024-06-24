"""Module for testing function time performance"""

import timeit

NUM_TESTS = 2000


# Another person's solution
MYSETUP = """
from number_of_islands import Solution
from test_cases import TestCases
"""
MYCODE = """
result_1 = Solution().num_islands_1(TestCases.test_1[0])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("num_islands_1() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYSETUP = """
from other_solution_2 import Solution as Solution2
from test_cases import TestCases
"""
MYCODE = """
result_1 = Solution2().num_islands_2(TestCases.test_1[0])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("num_islands_2() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYSETUP = """
from other_solution_3 import Solution as Solution3
from test_cases import TestCases
"""
MYCODE = """
result_1 = Solution3().num_islands_3(TestCases.test_1[0])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("num_islands_3() Running Time: " + TIME_PER_RUN)
