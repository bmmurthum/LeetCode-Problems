""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
from number_of_islands import Solution
from other_solution_2 import Solution as Solution2
from other_solution_3 import Solution as Solution3
from test_cases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    # My solution
    tracemalloc.start()
    result_1 = Solution().num_islands_1(TestCases.test_1[0])
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("number_of_islands.py Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    tracemalloc.start()
    result_2 = Solution2().num_islands_2(TestCases.test_1[0])
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("other_solution_1.py Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    tracemalloc.start()
    result_2 = Solution3().num_islands_3(TestCases.test_1[0])
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("other_solution_2.py Running: " + traced_memory_peak + " blocks")


run_memory_tests()
