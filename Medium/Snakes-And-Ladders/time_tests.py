"""Module for testing function time performance"""

import timeit

NUM_TESTS = 2000

# Test 10 - 2000 long, generated case.
MYSETUP = """
from snakes_and_ladders import Solution
from snakes_and_ladders_2 import Solution as Solution2
from testcases import TestCases
x = TestCases.test_10[0]
w = TestCases.test_7[0]
"""

print("Test 10: ")

# My depth-first solution
MYCODE = """
y = Solution().snakes_and_ladders(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("snakes_and_ladders() Running Time: " + TIME_PER_RUN)

# My breadth-first solution
MYCODE = """
y = Solution2().snakes_and_ladders_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("snakes_and_ladders_2() Running Time: " + TIME_PER_RUN)

print("Test 7: ")

# My depth-first solution
MYCODE = """
y = Solution().snakes_and_ladders(w)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("snakes_and_ladders() Running Time: " + TIME_PER_RUN)

# My breadth-first solution
MYCODE = """
y = Solution2().snakes_and_ladders_2(w)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("snakes_and_ladders_2() Running Time: " + TIME_PER_RUN)
