""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612

import tracemalloc
from gas_station import Solution
from gas_station_2 import Solution as Solution2
from gas_station_3 import Solution as Solution3
from gas_station_4 import Solution as Solution4
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

        #
        # TEST 8
        #
        case = TestCases.test_8
        x = case[0]
        y = case[1]
        string = case[3]
        print(f"\n{string}")
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        r = Solution().can_complete_circuit(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution2().can_complete_circuit_2(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution3().can_complete_circuit_3(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution4().can_complete_circuit_4(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_4()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Align function names to the right
        # Combine items and sort by blocks
        # Print all the functions and their block usage
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name
        combined_list = []
        for name, b in zip(function_list, block_list):
            combined_list.append([name, b])
        combined_list.sort(key=lambda a: int(a[1]))
        for item in combined_list:
            print(f"{self.padding}{item[0]}: {item[1]} blocks")

        #
        # TEST 9
        #
        case = TestCases.test_9
        x = case[0]
        y = case[1]
        string = case[3]
        print(f"\n{string}")
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        r = Solution().can_complete_circuit(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution2().can_complete_circuit_2(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution3().can_complete_circuit_3(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution4().can_complete_circuit_4(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_4()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Align function names to the right
        # Combine items and sort by blocks
        # Print all the functions and their block usage
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name
        combined_list = []
        for name, b in zip(function_list, block_list):
            combined_list.append([name, b])
        combined_list.sort(key=lambda a: int(a[1]))
        for item in combined_list:
            print(f"{self.padding}{item[0]}: {item[1]} blocks")

        #
        # TEST 10
        #
        case = TestCases.test_10
        x = case[0]
        y = case[1]
        string = case[3]
        print(f"\n{string}")
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        r = Solution().can_complete_circuit(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution2().can_complete_circuit_2(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution3().can_complete_circuit_3(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution4().can_complete_circuit_4(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_4()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Align function names to the right
        # Combine items and sort by blocks
        # Print all the functions and their block usage
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name
        combined_list = []
        for name, b in zip(function_list, block_list):
            combined_list.append([name, b])
        combined_list.sort(key=lambda a: int(a[1]))
        for item in combined_list:
            print(f"{self.padding}{item[0]}: {item[1]} blocks")

        #
        # TEST 11
        #
        case = TestCases.test_11
        x = case[0]
        y = case[1]
        string = case[3]
        print(f"\n{string}")
        function_list = []
        block_list = []
        length_list = []

        # My solution
        tracemalloc.start()
        r = Solution().can_complete_circuit(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution2().can_complete_circuit_2(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution3().can_complete_circuit_3(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Another person's solution
        tracemalloc.start()
        Solution4().can_complete_circuit_4(x, y)
        traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
        function_name = "can_complete_circuit_4()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        block_list.append(traced_memory_peak)

        # Align function names to the right
        # Combine items and sort by blocks
        # Print all the functions and their block usage
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name
        combined_list = []
        for name, b in zip(function_list, block_list):
            combined_list.append([name, b])
        combined_list.sort(key=lambda a: int(a[1]))
        for item in combined_list:
            print(f"{self.padding}{item[0]}: {item[1]} blocks")


# if __name__ == "__main__":
#     MemoryTests().run_memory_tests()
