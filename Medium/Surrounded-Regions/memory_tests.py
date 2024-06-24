""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
from surrounded_regions import Solution
from other_solution_2 import Solution as Solution2
from other_solution_3 import Solution as Solution3
from test_cases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    # My solution
    tracemalloc.start()
    result_1 = Solution().solve_1(TestCases.test_11[0])
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("solve_1() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    tracemalloc.start()
    result_2 = Solution2().solve_2(TestCases.test_11[0])
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("solve_2() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    tracemalloc.start()
    result_2 = Solution3().solve_3(TestCases.test_11[0])
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("solve_3() Running: " + traced_memory_peak + " blocks")


run_memory_tests()
