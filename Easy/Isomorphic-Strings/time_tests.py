"""Module for testing function time performance"""

import timeit

NUM_TESTS = 100

# Test 10 - 10x10 case.
MYSETUP = """
from isomorphic_strings import Solution
from isomorphic_strings_2 import Solution as Solution2
from isomorphic_strings_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_9[0]
y = TestCases.test_9[1]
"""

print("Test 9: Alphabet with false letter at end.")

# My solution
MYCODE = """
Solution().is_isomorphic(x,y)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("is_isomorphic() Running Time: " + TIME_PER_RUN)


# Another person's solution
MYCODE = """
Solution2().is_isomorphic_2(x,y)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("is_isomorphic_2() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
Solution3().is_isomorphic_3(x,y)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("is_isomorphic_3() Running Time: " + TIME_PER_RUN)
