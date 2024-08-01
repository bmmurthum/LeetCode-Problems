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
        # TEST 6
        #
        print("\nTestcase 6: 1000 Ones.")
        MYSETUP = """
from jump_game_ii import Solution
from jump_game_ii_2 import Solution as Solution2
from jump_game_ii_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_6[0]
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
Solution().jump(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "jump()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().jump_2(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "jump_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().jump_3(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "jump_3()"
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
        # TEST 7
        #
        print("\nTestcase 7: 1000 ones. Jumpable.")
        MYSETUP = """
from jump_game_ii import Solution
from jump_game_ii_2 import Solution as Solution2
from jump_game_ii_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_7[0]
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
Solution().jump(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "jump()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().jump_2(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "jump_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().jump_3(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "jump_3()"
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
