"""Module for performing unit-tests on my functions"""

import unittest
from rotate_image import Solution
from rotate_image_2 import Solution as Solution2
from rotate_image_3 import Solution as Solution3

from copy import deepcopy

from testcases import TestCases


class Testing(unittest.TestCase):
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.method_count = 5

    def which_method_to_test(self, which, x) -> int:
        """
        Handles testing multiple implementations of a given method.

        Args:
            `which`: Which method to test.
            `x`: A first input into the given method to test.
        """
        x = deepcopy(x)

        # Collection of solutions
        if which == 1:
            Solution().rotate(x)
            return x
        elif which == 2:
            Solution2().rotate_2(x)
            return x
        elif which == 3:
            Solution3().rotate_3(x)
            return x
        elif which == 4:
            Solution().rotate_b(x)
            return x
        elif which == 5:
            Solution().rotate_c(x)
            return x

    def test_1(self):
        """Test 1"""
        which_test = TestCases.test_1
        test_input = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_input)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_2(self):
        """Test 2"""
        which_test = TestCases.test_2
        test_input = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_input)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_3(self):
        """Test 3"""
        which_test = TestCases.test_3
        test_input = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_input)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_4(self):
        """Test 4"""
        which_test = TestCases.test_4
        test_input = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_input)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_5(self):
        """Test 5"""
        which_test = TestCases.test_5
        test_input = which_test[0]
        correct = which_test[1]
        test_description = which_test[2]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_input)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )
