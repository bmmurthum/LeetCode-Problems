"""Module for testing function time performance"""

import timeit


class TimeTests:
    """A collection of time tests for the tested methods."""

    # Number of tests on a single testcase.
    NUM_TESTS = 100
    # Left padding on runtime results.
    SOLUTION_PADDING = 4

    padding = ""
    for _ in range(SOLUTION_PADDING):
        padding += " "

    def run_time_tests(self):
        """Runs the collection of time tests"""

        print("\n** Time Tests **")

        # Test 9
        print("\nTestcase 9: 2000-long case.")
        function_list = []
        time_list = []
        length_list = []

        MYSETUP = """
from contains_duplicate_II import Solution
from testcases import TestCases
x = TestCases.test_9[0]
y = TestCases.test_9[1]
        """

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_a(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_a()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_b(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_c(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_c()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_d(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_d()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_e(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_e()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_f(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_f()"
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

        # Test 11
        print("\nTestcase 11: 2000-long case. No matches. K longer than list.")
        function_list = []
        time_list = []
        length_list = []

        MYSETUP = """
from contains_duplicate_II import Solution
from testcases import TestCases
x = TestCases.test_11[0]
y = TestCases.test_11[1]
        """

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_a(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_a()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_b(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_c(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_c()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_d(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_d()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_e(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_e()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_f(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_f()"
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

        # Test 5
        print("\nTestcase 5: k == 0.")
        function_list = []
        time_list = []
        length_list = []

        MYSETUP = """
from contains_duplicate_II import Solution
from testcases import TestCases
x = TestCases.test_5[0]
y = TestCases.test_5[1]
        """

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_a(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_a()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_b(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_c(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_c()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_d(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_d()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_e(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_e()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution
        MYCODE = """
Solution().contains_nearby_duplicate_f(x,y)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "contains_nearby_duplicate_f()"
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
