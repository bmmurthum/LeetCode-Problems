""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
import copy
from minimum_genetic_mutation import Solution
from minimum_genetic_mutation_2 import Solution as Solution2
from minimum_genetic_mutation_3 import Solution as Solution3
from testcases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    print("Test 4: ")

    # My solution
    test_start = TestCases.test_4[0]
    test_end = TestCases.test_4[1]
    test_list = copy.copy(TestCases.test_4[2])
    tracemalloc.start()
    result_1 = Solution().min_mutation(test_start, test_end, test_list)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("min_mutation() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    test_start = TestCases.test_4[0]
    test_end = TestCases.test_4[1]
    test_list = copy.copy(TestCases.test_4[2])
    tracemalloc.start()
    result_2 = Solution2().min_mutation_2(test_start, test_end, test_list)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("min_mutation_2() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    test_start = TestCases.test_4[0]
    test_end = TestCases.test_4[1]
    test_list = copy.copy(TestCases.test_4[2])
    tracemalloc.start()
    result_3 = Solution3().min_mutation_3(test_start, test_end, test_list)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("min_mutation_3() Running: " + traced_memory_peak + " blocks")


run_memory_tests()
