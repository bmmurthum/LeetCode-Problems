""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
import copy
from rotate_image import Solution
from rotate_image_2 import Solution as Solution2
from rotate_image_3 import Solution as Solution3
from testcases import TestCases

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    print("Test 2: ")

    # My solution
    x = copy.copy(TestCases.test_2[0])
    tracemalloc.start()
    result_1 = Solution().rotate(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate() Running: " + traced_memory_peak + " blocks")

    # My solution 2
    x = copy.copy(TestCases.test_2[0])
    tracemalloc.start()
    result_2 = Solution().rotate_b(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate_b() Running: " + traced_memory_peak + " blocks")

    # My solution 3
    x = copy.copy(TestCases.test_2[0])
    tracemalloc.start()
    result_2 = Solution().rotate_c(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate_c() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.copy(TestCases.test_2[0])
    tracemalloc.start()
    result_3 = Solution2().rotate_2(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate_2() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.copy(TestCases.test_2[0])
    tracemalloc.start()
    result_4 = Solution3().rotate_3(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate_3() Running: " + traced_memory_peak + " blocks")

    print("Test 5: ")

    # My solution
    x = copy.copy(TestCases.test_5[0])
    tracemalloc.start()
    result_5 = Solution().rotate(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate() Running: " + traced_memory_peak + " blocks")

    # My solution 2
    x = copy.copy(TestCases.test_5[0])
    tracemalloc.start()
    result_6 = Solution().rotate_b(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate_b() Running: " + traced_memory_peak + " blocks")

    # My solution 3
    x = copy.copy(TestCases.test_5[0])
    tracemalloc.start()
    result_2 = Solution().rotate_c(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate_c() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.copy(TestCases.test_5[0])
    tracemalloc.start()
    result_7 = Solution2().rotate_2(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate_2() Running: " + traced_memory_peak + " blocks")

    # Another person's solution
    x = copy.copy(TestCases.test_5[0])
    tracemalloc.start()
    result_8 = Solution3().rotate_3(x)
    traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("rotate_3() Running: " + traced_memory_peak + " blocks")


run_memory_tests()
