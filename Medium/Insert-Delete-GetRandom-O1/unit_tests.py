"""Module for performing unit-tests on my functions"""

import unittest
from contextlib import contextmanager
import sys
import os
from insert_delete_getrandom_o1 import RandomizedSet
from insert_delete_getrandom_o1_2 import RandomizedSet as RandomizedSet2


@contextmanager
def suppress_stdout():
    """Allows for running lines and suppressing its console output."""
    with open(os.devnull, "w", encoding="utf-8") as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr


METHOD_COUNT = 2


class Testing(unittest.TestCase):
    """
    Testing class for unittest library
    """

    def which_method_to_test(self, which) -> int:
        """
        Handles testing multiple implementations of a given method.

        Args:
            `which`: Which method to test.
            `x`: A first input into the given method to test.
        """

        # Collection of solutions
        if which == 1:
            z = RandomizedSet()
            return z
        elif which == 2:
            z = RandomizedSet2()
            return z

    def test_1(self):
        """Checking against LeetCode's Test"""
        correct = [True, False, True, "***", True, False, 2, True]
        test_description = "LeetCode's Example"
        for w in range(1, METHOD_COUNT + 1):
            obj = self.which_method_to_test(w)
            output = []
            output.append(obj.insert(1))
            output.append(obj.remove(2))
            output.append(obj.insert(2))
            output.append(obj.getRandom())
            output.append(obj.remove(1))
            output.append(obj.insert(2))
            output.append(obj.getRandom())
            output.append(obj.remove(2))
            # Affirms that this value is correct
            if output[3] == 1 or output[3] == 2:
                output[3] = "***"
            else:
                output[3] = "###"
            self.assertEqual(
                output,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )


class UnitTests:
    """Calls the unit-tests in minimal display format."""

    def run_unit_tests(self):
        """Calls the unit-tests in minimal display format."""

        r = None
        with suppress_stdout():
            temp = unittest.defaultTestLoader.loadTestsFromTestCase(Testing)
            runner = unittest.TextTestRunner()
            r = runner.run(temp)

        print("\n** Unit Tests **\n")

        print(f"Unit Tests Ran: {r.testsRun}")
        print(f"Methods Tested: {METHOD_COUNT}")
        print(f"Errors: {len(r.errors)}")
        print(f"Skipped: {len(r.skipped)}")
        print(f"Failures: {len(r.failures)}")


# if __name__ == "__main__":
#     unittest.main()
#     UnitTests().run_unit_tests()
