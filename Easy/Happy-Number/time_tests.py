"""Module for testing function time performance"""

import timeit
import random
import time
from happy_number import Solution
from happy_number_2 import Solution as Solution2
from happy_number_3 import Solution as Solution3
from happy_number_4 import Solution as Solution4


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

        # Test 9
        print("\nTestcase 9: Starting with 8.")
        function_list = []
        time_list = []
        length_list = []

        MYSETUP = """
from happy_number import Solution
from happy_number_2 import Solution as Solution2
from happy_number_3 import Solution as Solution3
from happy_number_4 import Solution as Solution4
from testcases import TestCases
x = TestCases.test_9[0]
        """

        # My solution
        MYCODE = """
Solution().is_happy(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution 2
        MYCODE = """
Solution().is_happy_b(x)
        """
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().is_happy_2(x)
        """
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().is_happy_3(x)
        """
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution4().is_happy_4(x)
        """
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy_4()"
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

        # Test 934063
        print("\nTestcase 24: Starting with 934063.")
        function_list = []
        time_list = []
        length_list = []

        MYSETUP = """
from happy_number import Solution
from happy_number_2 import Solution as Solution2
from happy_number_3 import Solution as Solution3
from happy_number_4 import Solution as Solution4
from testcases import TestCases
x = TestCases.test_24[0]
        """

        # My solution
        MYCODE = """
Solution().is_happy(x)"""
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # My solution 2
        MYCODE = """
Solution().is_happy_b(x)
        """
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution2().is_happy_2(x)
        """
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution3().is_happy_3(x)
        """
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(time_per_run)

        # Another person's solution
        MYCODE = """
Solution4().is_happy_4(x)
        """
        time_per_run = timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=self.NUM_TESTS)
        time_per_run = f"{time_per_run:.4e}"
        function_name = "is_happy_4()"
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

        # Solving a random set of 1000 integers being happy-numbers
        print("\nTestcase X: Solve many random cases.")
        NUM_CASES = 5000
        MIN_RAND = 1
        MAX_RAND = 4294967200
        function_list = []
        time_list = []
        length_list = []

        # My solution
        time_total = 0
        for _ in range(NUM_CASES):
            num = random.randint(MIN_RAND, MAX_RAND)
            t_start = time.time()
            Solution().is_happy(num)
            t_end = time.time()
            time_total += t_end - t_start
        TIME_PER_RUN = f"{(time_total / NUM_CASES):.4e}"
        function_name = "is_happy()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(TIME_PER_RUN)

        # My solution 2
        time_total = 0
        for _ in range(NUM_CASES):
            num = random.randint(MIN_RAND, MAX_RAND)
            t_start = time.time()
            Solution().is_happy_b(num)
            t_end = time.time()
            time_total += t_end - t_start
        TIME_PER_RUN = f"{(time_total / NUM_CASES):.4e}"
        function_name = "is_happy_b()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(TIME_PER_RUN)

        # Another person's solution
        time_total = 0
        for _ in range(NUM_CASES):
            num = random.randint(MIN_RAND, MAX_RAND)
            t_start = time.time()
            Solution2().is_happy_2(num)
            t_end = time.time()
            time_total += t_end - t_start
        TIME_PER_RUN = f"{(time_total / NUM_CASES):.4e}"
        function_name = "is_happy_2()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(TIME_PER_RUN)

        # Another person's solution
        time_total = 0
        for _ in range(NUM_CASES):
            num = random.randint(MIN_RAND, MAX_RAND)
            t_start = time.time()
            Solution3().is_happy_3(num)
            t_end = time.time()
            time_total += t_end - t_start
        TIME_PER_RUN = f"{(time_total / NUM_CASES):.4e}"
        function_name = "is_happy_3()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(TIME_PER_RUN)

        # Another person's solution
        time_total = 0
        for _ in range(NUM_CASES):
            num = random.randint(MIN_RAND, MAX_RAND)
            t_start = time.time()
            Solution4().is_happy_4(num)
            t_end = time.time()
            time_total += t_end - t_start
        TIME_PER_RUN = f"{(time_total / NUM_CASES):.4e}"
        function_name = "is_happy_4()"
        function_list.append(function_name)
        length_list.append(len(function_name))
        time_list.append(TIME_PER_RUN)

        # Align function names to the right
        m = max(length_list)
        for i, name in enumerate(function_list):
            while len(name) < m:
                name = " " + name
            function_list[i] = name

        # Print all the functions and their times
        for name, t in zip(function_list, time_list):
            print(f"{self.padding}{name} runtime: {t} sec")


if __name__ == "__main__":
    TimeTests().run_time_tests()
