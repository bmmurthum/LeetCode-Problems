"""Module for testing function time performance"""

import timeit

NUM_TESTS = 2000

# Test 7 - 5000 long, generated case.
print("5000-long list of three items - Test 7:")
MYSETUP = """
from majority_element import Solution
from other_solution_2 import Solution as Solution2
from other_solution_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_7[0]
"""

# My solution
MYCODE = """
y = Solution().majority_element(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("majority_element() Running Time: " + TIME_PER_RUN)

# My second solution
MYCODE = """
y = Solution().majority_element_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("majority_element_2() Running Time: " + TIME_PER_RUN)


# Another person's solution
MYCODE = """
y = Solution2().majority_element_3(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("majority_element_3() Running Time: " + TIME_PER_RUN)


# Another person's solution
MYCODE = """
y = Solution3().majority_element_4(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("majority_element_4() Running Time: " + TIME_PER_RUN)
