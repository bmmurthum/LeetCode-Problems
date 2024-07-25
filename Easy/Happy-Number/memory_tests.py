""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
from happy_number import Solution
from happy_number_2 import Solution as Solution2
from happy_number_3 import Solution as Solution3
from happy_number_4 import Solution as Solution4
from testcases import TestCases

# Testing Memory Allocation


class MemoryTests:
    """A collection of memory tests for the tested methods."""

    # Left padding on runtime results.
    SOLUTION_PADDING = 4

    padding = ""
    for _ in range(SOLUTION_PADDING):
        padding += " "

    def run_memory_tests(self):
        """Runs the collection of memory tests"""

        print("\n** Memory Tests **")

        print("\nTestcase 9: Starting with 8.")
        x = TestCases.test_9[0]
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        Solution().is_happy(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 2
        tracemalloc.start()
        Solution().is_happy_b(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution2().is_happy_2(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution3().is_happy_3(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution4().is_happy_4(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy_4()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Align function names to the right
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name

        # Print all the functions and their times
        for name, b in zip(function_list, block_list):
            print(f"{self.padding}{name}: {b} blocks")

        print("\nTestcase 24: Starting with 934063.")
        x = TestCases.test_24[0]
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        Solution().is_happy(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 2
        tracemalloc.start()
        Solution().is_happy_b(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution2().is_happy_2(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution3().is_happy_3(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution4().is_happy_4(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "is_happy_4()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Align function names to the right
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name

        # Print all the functions and their times
        for name, b in zip(function_list, block_list):
            print(f"{self.padding}{name}: {b} blocks")


# if __name__ == "__main__":
#     MemoryTests().run_memory_tests()
