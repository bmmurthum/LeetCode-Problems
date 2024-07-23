"""Module for testing function time performance"""

import timeit

NUM_TESTS = 100

# Test 10 - 10x10 case.
MYSETUP = """
from copy import deepcopy
from game_of_life import Solution
from game_of_life_2 import Solution as Solution2
from game_of_life_3 import Solution as Solution3
from testcases import TestCases
"""

print("Test 10: 10x10 case.")

# My solution
MYCODE = """
x = deepcopy(TestCases.test_10[0])
Solution().game_of_life(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("game_of_life() Running Time: " + TIME_PER_RUN)


# Another person's solution
MYCODE = """
x = deepcopy(TestCases.test_10[0])
Solution2().game_of_life_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("game_of_life_2() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
x = deepcopy(TestCases.test_10[0])
Solution3().game_of_life_3(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("game_of_life_3() Running Time: " + TIME_PER_RUN)
