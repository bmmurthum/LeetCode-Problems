""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
import copy
from remove_duplicates_from_sorted_array_2 import Solution
from other_solution_2 import Solution as Solution2
from other_solution_3 import Solution as Solution3
from test_cases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    # My solution
    x = copy.deepcopy(TestCases.test_8[0])
    tracemalloc.start()
    result_1 = Solution().remove_duplicates(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("remove_duplicates() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.deepcopy(TestCases.test_8[0])
    tracemalloc.start()
    result_2 = Solution2().remove_duplicates_2(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("remove_duplicates_2() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.deepcopy(TestCases.test_8[0])
    tracemalloc.start()
    result_3 = Solution3().remove_duplicates_3(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("remove_duplicates_3() Running: " + traced_memory_peak + " blocks")


run_memory_tests()
