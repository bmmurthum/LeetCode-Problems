""" Module to report peak-memory used by method """

# Unused variable. We use this on returning a result to check memory usage.
# pylint: disable=W0612
# Allowing eval()
# pylint: disable=W0123
# Allowing exec()
# pylint: disable=W0122
# Allowing "unused import". TestCases is used in an eval().
# pylint: disable=W0611

import tracemalloc
from candy import Solution
from candy_2 import Solution as Solution2
from candy_3 import Solution as Solution3
from candy_4 import Solution as Solution4
from testcases import TestCases

# Testing Memory Allocation


class MemoryTests:
    """A collection of memory tests for the tested methods."""

    # Left padding on runtime results.
    SOLUTION_PADDING = 4

    padding = ""
    for _ in range(SOLUTION_PADDING):
        padding += " "

    # Confirm each test's one-time ran variable initialization
    variable_setup = """
case = TestCases.TEST
x = case[0]
"""

    # Confirm this is the format of the many-times ran code.
    code_setup = "IMPORT().METHOD(x)"

    # Confirm these at the imported class names
    import_names = ["Solution", "Solution2", "Solution3", "Solution4"]

    # Confirm these as the associated method names
    function_names = [
        "candy",
        "candy_2",
        "candy_3",
        "candy_4",
    ]

    # Confirm these as the tests to run on those methods
    test_variable_names = ["test_10", "test_11", "test_12", "test_13"]

    def run_memory_tests(self):
        """Runs the collection of memory tests"""

        print("\n** Memory Tests**\n")

        for test_name in self.test_variable_names:

            # Print the test's description
            test_description = eval(f"TestCases.{test_name}[-1]")
            print(test_description)

            # Setting up a testcase
            case = eval(f"TestCases.{test_name}")
            x = case[0]
            y = case[1]
            function_list = []
            block_list = []
            length_list = []

            # Running each method on that testcase
            for i, method_name in enumerate(self.function_names):

                # Prep code to run
                run_code = self.code_setup
                run_code = run_code.replace("IMPORT", self.import_names[i])
                run_code = run_code.replace("METHOD", method_name)

                # Run a test
                tracemalloc.start()
                exec(run_code)
                traced_memory_peak = str(tracemalloc.get_traced_memory()[1])
                tracemalloc.stop()
                function_name = f"{method_name}()"
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

            print("")


# if __name__ == "__main__":
#     MemoryTests().run_memory_tests()
