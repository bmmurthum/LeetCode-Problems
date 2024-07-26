""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
from linked_list_cycle import Solution
from linked_list_cycle_2 import Solution as Solution2
from linked_list_cycle_3 import Solution as Solution3
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

        print("\nTestcase 5: 12-long linked-list without cycle.")
        x = TestCases.test_5[0]
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        Solution().has_cycle(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "has_cycle()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution2().has_cycle_2(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "has_cycle_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution3().has_cycle_3(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "has_cycle_3()"
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

        print("\nTestcase 6: 12-long linked-list with cycle.")
        x = TestCases.test_6[0]
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        Solution().has_cycle(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "has_cycle()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution2().has_cycle_2(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "has_cycle_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution3().has_cycle_3(x)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "has_cycle_3()"
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
