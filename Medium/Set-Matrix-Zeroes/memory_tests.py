""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
import copy
from set_matrix_zeroes import Solution
from set_matrix_zeroes_2 import Solution as Solution2
from set_matrix_zeroes_3 import Solution as Solution3
from set_matrix_zeroes_4 import Solution as Solution4
from testcases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    print("Test 9: ")

    # My solution
    x = copy.copy(TestCases.test_9[0])
    tracemalloc.start()
    Solution().set_zeroes(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("set_zeroes() Running: " + traced_memory_peak + " blocks")

    # My solution 2
    x = copy.copy(TestCases.test_9[0])
    tracemalloc.start()
    Solution().set_zeroes_b(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("set_zeroes_b() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.copy(TestCases.test_9[0])
    tracemalloc.start()
    Solution2().set_zeroes_2(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("set_zeroes_2() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.copy(TestCases.test_9[0])
    tracemalloc.start()
    Solution3().set_zeroes_3(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("set_zeroes_3() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.copy(TestCases.test_9[0])
    tracemalloc.start()
    Solution4().set_zeroes_4(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("set_zeroes_4() Running: " + traced_memory_peak + " blocks")


run_memory_tests()
