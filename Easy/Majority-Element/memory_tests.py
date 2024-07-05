""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
import copy
from majority_element import Solution
from other_solution_2 import Solution as Solution2
from other_solution_3 import Solution as Solution3
from testcases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    # My solution
    x = copy.deepcopy(TestCases.test_7[0])
    tracemalloc.start()
    result_1 = Solution().majority_element(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("majority_element() Running: " + traced_memory_peak + " blocks")

    # Second solution
    x = copy.deepcopy(TestCases.test_7[0])
    tracemalloc.start()
    result_2 = Solution().majority_element_2(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("majority_element_2() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.deepcopy(TestCases.test_7[0])
    tracemalloc.start()
    result_3 = Solution2().majority_element_3(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("majority_element_3() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.deepcopy(TestCases.test_7[0])
    tracemalloc.start()
    result_4 = Solution3().majority_element_4(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("majority_element_4() Running: " + traced_memory_peak + " blocks")


run_memory_tests()
