"""Module for testing function time performance"""

import timeit


class TimeTests:
    """A collection of time tests for the tested methods."""

    # Number of tests on a single testcase.
    NUM_TESTS = 1000
    # Left padding on runtime results.
    SOLUTION_PADDING = 4

    padding = ""
    for _ in range(SOLUTION_PADDING):
        padding += " "

    def run_time_tests(self):
        """Runs the collection of time tests"""

        print("\n** Time Tests **")

        # Test 8
        print("\nTestcase 8: 20-long chain. 30 total values.")
        function_list = []
        time_list = []
        length_list = []

        MYSETUP = """
from longest_consecutive_sequence import Solution
from longest_consecutive_sequence_2 import Solution as Solution2
from longest_consecutive_sequence_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_8[0]
        """

        # My solution
        MYCODE = """
Solution().longest_consecutive(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "longest_consecutive()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().longest_consecutive_2(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "longest_consecutive_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().longest_consecutive_3(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "longest_consecutive_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Align function names to the right
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name

        # Print all the functions and their times
        for name, t in zip(function_list, time_list):
            print(f"{self.padding}{name} runtime: {t} sec")


# if __name__ == "__main__":
#     TimeTests().run_time_tests()
