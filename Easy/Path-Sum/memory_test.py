""" Module to report peak-memory used by method """

# pylint: disable=W0622

import tracemalloc
from path_sum import Solution
from path_sum_2 import Solution as Solution2
from path_sum_3 import Solution as Solution3
from test_cases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    # My solution
    tracemalloc.start()
    s = Solution()
    result_1 = s.has_path_sum_1(TestCases.test_3[0], TestCases.test_3[1])
    TRACED_MEMORY_PEAK_1 = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("has_path_sum_1() Running: " + TRACED_MEMORY_PEAK_1 + " blocks")

    # Another person's solution
    tracemalloc.start()
    s = Solution2()
    result_1 = s.has_path_sum_2(TestCases.test_3[0], TestCases.test_3[1])
    TRACED_MEMORY_PEAK_1 = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("has_path_sum_2() Running: " + TRACED_MEMORY_PEAK_1 + " blocks")

    # Another person's solution
    tracemalloc.start()
    s = Solution3()
    result_1 = s.has_path_sum_3(TestCases.test_3[0], TestCases.test_3[1])
    TRACED_MEMORY_PEAK_1 = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("has_path_sum_3() Running: " + TRACED_MEMORY_PEAK_1 + " blocks")


run_memory_tests()
