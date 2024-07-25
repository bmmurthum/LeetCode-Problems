""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
from contains_duplicate_II import Solution
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

        print("\nTestcase 9: 2000-long case.")
        x = TestCases.test_9[0]
        y = TestCases.test_9[1]
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        Solution().contains_nearby_duplicate_a(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_a()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 2
        tracemalloc.start()
        Solution().contains_nearby_duplicate_b(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 3
        tracemalloc.start()
        Solution().contains_nearby_duplicate_c(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_c()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 4
        tracemalloc.start()
        Solution().contains_nearby_duplicate_d(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_d()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 5
        tracemalloc.start()
        Solution().contains_nearby_duplicate_e(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_e()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 6
        tracemalloc.start()
        Solution().contains_nearby_duplicate_f(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_f()"
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

        print("\nTestcase 11: 2000-long case. No matches. K longer than list.")
        x = TestCases.test_11[0]
        y = TestCases.test_11[1]
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        Solution().contains_nearby_duplicate_a(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_a()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 2
        tracemalloc.start()
        Solution().contains_nearby_duplicate_b(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 3
        tracemalloc.start()
        Solution().contains_nearby_duplicate_c(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_c()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 4
        tracemalloc.start()
        Solution().contains_nearby_duplicate_d(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_d()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 5
        tracemalloc.start()
        Solution().contains_nearby_duplicate_e(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_e()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # My solution 6
        tracemalloc.start()
        Solution().contains_nearby_duplicate_f(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "contains_nearby_duplicate_f()"
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
