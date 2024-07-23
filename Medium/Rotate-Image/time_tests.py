"""Module for testing function time performance"""

import timeit

NUM_TESTS = 2000

# Test 2 - LeetCode Example.
MYSETUP = """
from rotate_image import Solution
from rotate_image_2 import Solution as Solution2
from rotate_image_3 import Solution as Solution3
from testcases import TestCases
"""

print("Test 2: ")

# My solution
MYCODE = """
x = TestCases.test_2[0]
result_1 = Solution().rotate(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate() Running Time: " + TIME_PER_RUN)

# My solution 2
MYCODE = """
x = TestCases.test_2[0]
result_1 = Solution().rotate_b(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_b() Running Time: " + TIME_PER_RUN)

# My solution 3
MYCODE = """
x = TestCases.test_2[0]
result_1 = Solution().rotate_c(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_c() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
x = TestCases.test_2[0]
result_2 = Solution2().rotate_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_2() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
x = TestCases.test_2[0]
result_3 = Solution3().rotate_3(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_3() Running Time: " + TIME_PER_RUN)


print("Test 5: ")

# My solution
MYCODE = """
x = TestCases.test_5[0]
result_1 = Solution().rotate(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate() Running Time: " + TIME_PER_RUN)

# My solution 2
MYCODE = """
x = TestCases.test_5[0]
result_1 = Solution().rotate_b(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_b() Running Time: " + TIME_PER_RUN)

# My solution 3
MYCODE = """
x = TestCases.test_5[0]
result_1 = Solution().rotate_c(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_c() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
x = TestCases.test_5[0]
result_2 = Solution2().rotate_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_2() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
x = TestCases.test_5[0]
result_3 = Solution3().rotate_3(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("rotate_3() Running Time: " + TIME_PER_RUN)
