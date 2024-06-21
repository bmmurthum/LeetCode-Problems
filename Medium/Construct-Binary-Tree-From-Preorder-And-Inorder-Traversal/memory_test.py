""" Module to report peak-memory used by method """

# pylint: disable=W0622

import tracemalloc
from construct_binary_tree_from_preorder import Solution
from other_solution import Solution as Solution2
from test_cases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    # My solution
    s = Solution()
    tracemalloc.start()
    result_1 = s.build_tree_1(TestCases.test_2[0], TestCases.test_2[1])
    TRACED_MEMORY_PEAK_1 = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("max_depth_1 Running: " + TRACED_MEMORY_PEAK_1 + " blocks")

    # My solution, without assigning results to variables internally
    t = Solution2()
    tracemalloc.start()
    result_2 = t.build_tree_2(TestCases.test_2[0], TestCases.test_2[1])
    TRACED_MEMORY_PEAK_2 = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("max_depth_2 Running: " + TRACED_MEMORY_PEAK_2 + " blocks")


run_memory_tests()
