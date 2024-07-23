""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
from copy import deepcopy
from game_of_life import Solution
from game_of_life_2 import Solution as Solution2
from game_of_life_3 import Solution as Solution3
from testcases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    print("Test 10: ")

    # My solution
    x = deepcopy(TestCases.test_10[0])
    tracemalloc.start()
    Solution().game_of_life(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("game_of_life() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = deepcopy(TestCases.test_10[0])
    tracemalloc.start()
    Solution2().game_of_life_2(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("game_of_life_2() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = deepcopy(TestCases.test_10[0])
    tracemalloc.start()
    Solution3().game_of_life_3(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("game_of_life_3() Running: " + traced_memory_peak + " blocks")


run_memory_tests()
