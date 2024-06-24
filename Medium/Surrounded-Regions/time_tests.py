"""Module for testing function time performance"""

import timeit

NUM_TESTS = 2000
from surrounded_regions import Solution

# Test 11 - Small regions
print("Small regions - Test 11:")

# My solution
MYSETUP = """
from surrounded_regions import Solution
from test_cases import TestCases
"""
MYCODE = """
x = TestCases.test_11[0]
Solution().solve_1(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("solve_1() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYSETUP = """
from other_solution_2 import Solution
from test_cases import TestCases
"""
MYCODE = """
x = TestCases.test_11[0]
Solution().solve_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("solve_2() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYSETUP = """
from other_solution_3 import Solution
from test_cases import TestCases
"""
MYCODE = """
x = TestCases.test_11[0]
Solution().solve_3(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("solve_3() Running Time: " + TIME_PER_RUN)


# Test 6 - No surrounds
print("No surrounds - Test 6:")


# My solution
MYSETUP = """
from surrounded_regions import Solution
from test_cases import TestCases
"""
MYCODE = """
x = TestCases.test_6[0]
Solution().solve_1(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("solve_1() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYSETUP = """
from other_solution_2 import Solution
from test_cases import TestCases
"""
MYCODE = """
x = TestCases.test_6[0]
Solution().solve_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("solve_2() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYSETUP = """
from other_solution_3 import Solution
from test_cases import TestCases
"""
MYCODE = """
x = TestCases.test_6[0]
Solution().solve_3(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("solve_3() Running Time: " + TIME_PER_RUN)
