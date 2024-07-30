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
        # TEST 9
        #
        print("\nTestcase 9: 1000 items, best sell at end.")
        MYSETUP = """
from best_time_to_buy_and_sell_stock_ii import Solution
from best_time_to_buy_and_sell_stock_ii_2 import Solution as Solution2
from best_time_to_buy_and_sell_stock_ii_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_9[0]
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
Solution().max_profit(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "max_profit()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().max_profit_2(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "max_profit_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().max_profit_3(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "max_profit_3()"
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
        # TEST 10
        #
        print("\nTestcase 10: 1000 items, best sell near beginning.")
        MYSETUP = """
from best_time_to_buy_and_sell_stock_ii import Solution
from best_time_to_buy_and_sell_stock_ii_2 import Solution as Solution2
from best_time_to_buy_and_sell_stock_ii_3 import Solution as Solution3
from testcases import TestCases
x = TestCases.test_10[0]
        """
        function_list = []
        time_list = []
        length_list = []

        # My solution
        MYCODE = """
Solution().max_profit(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "max_profit()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().max_profit_2(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "max_profit_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().max_profit_3(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "max_profit_3()"
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
