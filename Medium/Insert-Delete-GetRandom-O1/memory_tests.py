""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
from insert_delete_getrandom_o1 import RandomizedSet
from insert_delete_getrandom_o1_2 import RandomizedSet as RandomizedSet2

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

        #
        # TEST 1
        #
        print("\nTestcase 1: LeetCode Example.")
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        obj = RandomizedSet()
        obj.insert(1)
        obj.remove(2)
        obj.insert(2)
        obj.getRandom()
        obj.remove(1)
        obj.insert(2)
        obj.getRandom()
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "My Solution"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        obj_2 = RandomizedSet2()
        obj_2.insert(1)
        obj_2.remove(2)
        obj_2.insert(2)
        obj_2.getRandom()
        obj_2.remove(1)
        obj_2.insert(2)
        obj_2.getRandom()
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "Someone's Solution"
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
