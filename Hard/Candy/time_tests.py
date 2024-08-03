"""Module for testing function time performance"""

# Allowing eval()
# pylint: disable=W0123
# Allowing "unused import". TestCases is used in an eval().
# pylint: disable=W0611

import timeit
from testcases import TestCases


class TimeTests:
    """A collection of time tests for the tested methods."""

    # Number of tests on a single testcase.
    NUM_TESTS = 500
    # Left padding on runtime results.
    SOLUTION_PADDING = 4
    padding = ""
    for _ in range(SOLUTION_PADDING):
        padding += " "

    # Confirm the imports
    imports = """
from candy import Solution
from candy_2 import Solution as Solution2
from candy_3 import Solution as Solution3
from candy_4 import Solution as Solution4
from testcases import TestCases
"""

    # Confirm each test's one-time ran variable initialization
    variable_setup = """
case = TestCases.TEST
x = case[0]
"""

    # Confirm this is the format of the many-times ran code.
    code_setup = """
IMPORT().METHOD(x)"""

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

    # Auto generate the tests from the inputs above.
    def run_time_tests(self):
        """Runs the collection of time tests"""

        print("\n** Time Tests **\n")

        for test_name in self.test_variable_names:

            # Print the test's description
            test_description = eval(f"TestCases.{test_name}[-1]")
            print(test_description)

            # Test setup
            var_setup = self.variable_setup
            var_setup = var_setup.replace("TEST", test_name)
            test_setup = f"""
{self.imports}
{var_setup}
        """
            function_list = []
            length_list = []
            time_list = []

            # Running each method
            for i, method_name in enumerate(self.function_names):
                run_code = self.code_setup
                run_code = run_code.replace("IMPORT", self.import_names[i])
                run_code = run_code.replace("METHOD", method_name)
                time_per_run = timeit.timeit(
                    setup=test_setup, stmt=run_code, number=self.NUM_TESTS
                )
                function_name = f"{method_name}()"
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

            print("")


# if __name__ == "__main__":
#     TimeTests().run_time_tests()
