""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
from isomorphic_strings import Solution
from isomorphic_strings_2 import Solution as Solution2
from isomorphic_strings_3 import Solution as Solution3
from testcases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    print("Test 9: ")
    x = TestCases.test_9[0]
    y = TestCases.test_9[1]

    # My solution
    tracemalloc.start()
    Solution().is_isomorphic(x, y)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("is_isomorphic() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    tracemalloc.start()
    Solution2().is_isomorphic_2(x, y)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("is_isomorphic_2() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    tracemalloc.start()
    Solution3().is_isomorphic_3(x, y)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("is_isomorphic_3() Running: " + traced_memory_peak + " blocks")


run_memory_tests()
