"""Module for testing function time performance"""

import timeit


class TimeTests:
    """A collection of time tests for the tested methods."""

    # Number of tests on a single testcase.
    NUM_TESTS = 250
    # Left padding on runtime results.
    SOLUTION_PADDING = 4

    padding = ""
    for _ in range(SOLUTION_PADDING):
        padding += " "

    def run_time_tests(self):
        """Runs the collection of time tests"""

        print("\n** Time Tests **")

        #
        # TEST 1
        #
        print("\nTestcase 1: LeetCode's Example.")
        MYSETUP = """
from insert_delete_getrandom_o1 import RandomizedSet
from insert_delete_getrandom_o1_2 import RandomizedSet as RandomizedSet2
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
obj = RandomizedSet()
obj.insert(1)
obj.remove(2)
obj.insert(2)
obj.getRandom()
obj.remove(1)
obj.insert(2)
obj.getRandom()
"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "My Solution"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
obj = RandomizedSet2()
obj.insert(1)
obj.remove(2)
obj.insert(2)
obj.getRandom()
obj.remove(1)
obj.insert(2)
obj.getRandom()
"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "Someone's Solution"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Align function names to the right
        # Print all the functions and their times
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name
        for name, t in zip(function_list, time_list):
            print(f"{self.padding}{name} runtime: {t} sec")

        #
        # TEST 2
        #
        print("\nTestcase 2: All Inserts.")
        MYSETUP = """
from insert_delete_getrandom_o1 import RandomizedSet
from insert_delete_getrandom_o1_2 import RandomizedSet as RandomizedSet2
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
obj = RandomizedSet()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.insert(6)
obj.insert(7)
obj.insert(8)
obj.insert(9)
obj.insert(10)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "My Solution"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
obj = RandomizedSet2()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.insert(6)
obj.insert(7)
obj.insert(8)
obj.insert(9)
obj.insert(10)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.insert(1)
"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "Someone's Solution"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Align function names to the right
        # Print all the functions and their times
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name
        for name, t in zip(function_list, time_list):
            print(f"{self.padding}{name} runtime: {t} sec")

        #
        # TEST 3
        #
        print("\nTestcase 3: Random Heavy.")
        MYSETUP = """
from insert_delete_getrandom_o1 import RandomizedSet
from insert_delete_getrandom_o1_2 import RandomizedSet as RandomizedSet2
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
obj = RandomizedSet()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "My Solution"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
obj = RandomizedSet2()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
obj.getRandom()
"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "Someone's Solution"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Align function names to the right
        # Print all the functions and their times
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name
        for name, t in zip(function_list, time_list):
            print(f"{self.padding}{name} runtime: {t} sec")


# if __name__ == "__main__":
#     TimeTests().run_time_tests()
