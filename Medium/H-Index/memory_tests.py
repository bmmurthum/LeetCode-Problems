""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
import copy
from h_index import Solution
from other_solution_2 import Solution as Solution2
from testcases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    # My solution
    x = copy.deepcopy(TestCases.test_10[0])
    tracemalloc.start()
    result_1 = Solution().h_index(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("h_index() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.deepcopy(TestCases.test_10[0])
    tracemalloc.start()
    result_2 = Solution2().h_index_2(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("h_index_2() Running: " + traced_memory_peak + " blocks")


run_memory_tests()
