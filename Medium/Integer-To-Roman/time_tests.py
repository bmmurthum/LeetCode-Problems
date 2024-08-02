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
        print("\nTestcase 1: LeetCode Example 3749.")
        MYSETUP = """
from integer_to_roman import Solution
from integer_to_roman_2 import Solution as Solution2
from integer_to_roman_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_1[0]
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
Solution().int_to_roman(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = time_per_run
        function_name = "int_to_roman()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().int_to_roman_2(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = time_per_run
        function_name = "int_to_roman_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().int_to_roman_3(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = time_per_run
        function_name = "int_to_roman_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Align function names to the right
        # Combine items and sort by time
        # Print all the functions and their times
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name
        combined_list = []
        for name, t in zip(function_list, time_list):
            combined_list.append([name, t])
        combined_list.sort(key=lambda a: a[1])
        for item in combined_list:
            string = f"{item[1]:.3e}"
            pos_neg_sign = string[-3]
            mult = None
            if int(string[-2:]) < 10:
                mult = string[-1:]
            else:
                mult = string[-2:]
            num = string[:5]
            print(
                f"{self.padding}{item[0]} runtime: {num} x (10 ^ {pos_neg_sign}{mult}) sec"
            )

        #
        # TEST 3
        #
        print("\nTestcase 3: LeetCode Example 1994.")
        MYSETUP = """
from integer_to_roman import Solution
from integer_to_roman_2 import Solution as Solution2
from integer_to_roman_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_3[0]
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
Solution().int_to_roman(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = time_per_run
        function_name = "int_to_roman()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().int_to_roman_2(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = time_per_run
        function_name = "int_to_roman_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().int_to_roman_3(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = time_per_run
        function_name = "int_to_roman_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Align function names to the right
        # Combine items and sort by time
        # Print all the functions and their times
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name
        combined_list = []
        for name, t in zip(function_list, time_list):
            combined_list.append([name, t])
        combined_list.sort(key=lambda a: a[1])
        for item in combined_list:
            string = f"{item[1]:.3e}"
            pos_neg_sign = string[-3]
            mult = None
            if int(string[-2:]) < 10:
                mult = string[-1:]
            else:
                mult = string[-2:]
            num = string[:5]
            print(
                f"{self.padding}{item[0]} runtime: {num} x (10 ^ {pos_neg_sign}{mult}) sec"
            )


# if __name__ == "__main__":
#     TimeTests().run_time_tests()
