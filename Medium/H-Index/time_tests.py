"""Module for testing function time performance"""

import timeit

NUM_TESTS = 2000

# Test 10 - 2000 long, generated case.
MYSETUP = """
from h_index import Solution
from other_solution_2 import Solution as Solution2
from testcases import TestCases
x = TestCases.test_10[0]
w = TestCases.test_7[0]
"""

print("Test 10: ")

# My solution
MYCODE = """
y = Solution().h_index(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("h_index() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
y = Solution2().h_index_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("h_index_2() Running Time: " + TIME_PER_RUN)

print("Test 7: ")

# My solution
MYCODE = """
y = Solution().h_index(w)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("h_index() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
y = Solution2().h_index_2(w)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("h_index_2() Running Time: " + TIME_PER_RUN)
