"""Module for testing function time performance"""

import timeit


class TimeTests:
    """A collection of time tests for the tested methods."""

    # Number of tests on a single testcase.
    NUM_TESTS = 500
    # Left padding on runtime results.
    SOLUTION_PADDING = 4

    padding = ""
    for _ in range(SOLUTION_PADDING):
        padding += " "

    def run_time_tests(self):
        """Runs the collection of time tests"""

        print("\n** Time Tests **")

        #
        # TEST 7
        #
        print("\nTestcase 7: 15-long linked-list.")
        MYSETUP = """
from copy_list_with_random_pointer import Solution
from copy_list_with_random_pointer_2 import Solution as Solution2
from copy_list_with_random_pointer_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_7[0]
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
Solution().copy_random_list(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "copy_random_list()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().copy_random_list_2(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "copy_random_list_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().copy_random_list_3(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "copy_random_list_3()"
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
