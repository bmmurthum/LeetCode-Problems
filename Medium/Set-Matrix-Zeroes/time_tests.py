"""Module for testing function time performance"""

import timeit

NUM_TESTS = 50

# Test 9 - Generated 150x180 case.
MYSETUP = """
from set_matrix_zeroes import Solution
from set_matrix_zeroes_2 import Solution as Solution2
from set_matrix_zeroes_3 import Solution as Solution3
from set_matrix_zeroes_4 import Solution as Solution4
from testcases import TestCases
"""

print("Test 9: Generated 150x180 case.")

# My solution
MYCODE = """
x = TestCases.test_9[0]
Solution().set_zeroes(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("set_zeroes() Running Time: " + TIME_PER_RUN)

# My solution 2
MYCODE = """
x = TestCases.test_9[0]
Solution().set_zeroes_b(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("set_zeroes_b() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
x = TestCases.test_9[0]
Solution2().set_zeroes_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("set_zeroes_2() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
x = TestCases.test_9[0]
Solution3().set_zeroes_3(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("set_zeroes_3() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
x = TestCases.test_9[0]
Solution4().set_zeroes_4(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("set_zeroes_4() Running Time: " + TIME_PER_RUN)
