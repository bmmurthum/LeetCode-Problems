""" Module to report peak-memory used by method """

import tracemalloc

from maximum_depth_of_binary_tree import Solution
from maximum_depth_of_binary_tree_2 import Solution as Solution2
from test_cases import TestCases

# pylint: disable=W0622

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    # My solution
    s = Solution()
    tracemalloc.start()
    result_1 = s.max_depth_1(TestCases.test_1_head)
    TRACED_MEMORY_PEAK_1 = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("max_depth_1 Running: " + TRACED_MEMORY_PEAK_1 + " blocks")

    # My solution, without assigning results to variables internally
    t = Solution2()
    tracemalloc.start()
    result_2 = t.max_depth_2(TestCases.test_1_head)
    TRACED_MEMORY_PEAK_2 = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("max_depth_2 Running: " + TRACED_MEMORY_PEAK_2 + " blocks")


run_memory_tests()
