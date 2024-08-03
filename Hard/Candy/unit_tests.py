"""Module for performing unit-tests on my functions"""

import unittest
from contextlib import contextmanager
import sys
import os
from candy import Solution
from candy_2 import Solution as Solution2
from candy_3 import Solution as Solution3
from candy_4 import Solution as Solution4
from testcases import TestCases


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


METHOD_COUNT = 4


class Testing(unittest.TestCase):
    """
    Testing class for unittest library
    """

    def which_method_to_test(self, which, x) -> int:
        """
        Handles testing multiple implementations of a given method.

        Args:
            `which`: Which method to test.
            `x`: A first input into the given method to test.
            `y`: A second input into the given method to test.
        """

        # Collection of solutions
        if which == 1:
            z = Solution().candy(x)
            return z
        elif which == 2:
            z = Solution2().candy_2(x)
            return z
        elif which == 3:
            z = Solution3().candy_3(x)
            return z
        elif which == 4:
            z = Solution4().candy_4(x)
            return z

    def test_1(self):
        """Test 1"""
        which_test = TestCases.test_1
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_2(self):
        """Test 2"""
        which_test = TestCases.test_2
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_3(self):
        """Test 3"""
        which_test = TestCases.test_3
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_4(self):
        """Test 4"""
        which_test = TestCases.test_4
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_5(self):
        """Test 5"""
        which_test = TestCases.test_5
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_6(self):
        """Test 6"""
        which_test = TestCases.test_6
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_7(self):
        """Test 7"""
        which_test = TestCases.test_7
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_8(self):
        """Test 8"""
        which_test = TestCases.test_8
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_9(self):
        """Test 9"""
        which_test = TestCases.test_9
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_10(self):
        """Test 10"""
        which_test = TestCases.test_10
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_11(self):
        """Test 11"""
        which_test = TestCases.test_11
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_12(self):
        """Test 12"""
        which_test = TestCases.test_12
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_13(self):
        """Test 13"""
        which_test = TestCases.test_13
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_14(self):
        """Test 14"""
        which_test = TestCases.test_14
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_15(self):
        """Test 15"""
        which_test = TestCases.test_15
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_16(self):
        """Test 16"""
        which_test = TestCases.test_16
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_17(self):
        """Test 17"""
        which_test = TestCases.test_17
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_18(self):
        """Test 18"""
        which_test = TestCases.test_18
        test_input_1 = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, METHOD_COUNT + 1):
            result = self.which_method_to_test(w, test_input_1)
            self.assertEqual(
                result,
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
