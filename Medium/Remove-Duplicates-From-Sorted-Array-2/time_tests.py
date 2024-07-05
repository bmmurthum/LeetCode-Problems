"""Module for testing function time performance"""

import timeit

NUM_TESTS = 2000

# Test 11 - Small regions
print("Large list of two items - Test 8:")
MYSETUP = """
from remove_duplicates_from_sorted_array_2 import Solution
from other_solution_2 import Solution as Solution2
from other_solution_3 import Solution as Solution3
from test_cases import TestCases
x = TestCases.test_8[0]
"""

# My solution
MYCODE = """
y = Solution().remove_duplicates(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("remove_duplicates() Running Time: " + TIME_PER_RUN)

# Someone else's solution
MYCODE = """
y = Solution2().remove_duplicates_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("remove_duplicates_2() Running Time: " + TIME_PER_RUN)

# Someone else's solution
MYCODE = """
y = Solution3().remove_duplicates_3(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("remove_duplicates_3() Running Time: " + TIME_PER_RUN)
print("")


# Test 2 - LeetCode example case.
print("LeetCode example case - Test 2:")
MYSETUP = """
from remove_duplicates_from_sorted_array_2 import Solution
from other_solution_2 import Solution as Solution2
from other_solution_3 import Solution as Solution3
from test_cases import TestCases
x = TestCases.test_2[0]
"""

# My solution
MYCODE = """
y = Solution().remove_duplicates(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("remove_duplicates() Running Time: " + TIME_PER_RUN)

# Someone else's solution
MYCODE = """
y = Solution2().remove_duplicates_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("remove_duplicates_2() Running Time: " + TIME_PER_RUN)

# Someone else's solution
MYCODE = """
y = Solution3().remove_duplicates_3(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("remove_duplicates_3() Running Time: " + TIME_PER_RUN)
print("")
