"""Module for testing function time performance"""

import timeit

NUM_TESTS = 2000

# Test 4 - A case with several mutation steps.
MYSETUP = """
from minimum_genetic_mutation import Solution
from minimum_genetic_mutation_2 import Solution as Solution2
from minimum_genetic_mutation_3 import Solution as Solution3
from testcases import TestCases
"""

print("Test 4: ")

# My solution
MYCODE = """
test_start = TestCases.test_4[0]
test_end = TestCases.test_4[1]
test_list = TestCases.test_4[2]
result_1 = Solution().min_mutation(test_start, test_end, test_list)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("min_mutation() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
test_start = TestCases.test_4[0]
test_end = TestCases.test_4[1]
test_list = TestCases.test_4[2]
result_2 = Solution2().min_mutation_2(test_start, test_end, test_list)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("min_mutation_2() Running Time: " + TIME_PER_RUN)

# Another person's solution
MYCODE = """
test_start = TestCases.test_4[0]
test_end = TestCases.test_4[1]
test_list = TestCases.test_4[2]
result_3 = Solution3().min_mutation_3(test_start, test_end, test_list)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("min_mutation_3() Running Time: " + TIME_PER_RUN)
