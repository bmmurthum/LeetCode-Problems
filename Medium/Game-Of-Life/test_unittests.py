"""Module for performing unit-tests on my functions"""

import unittest
from game_of_life import Solution
from game_of_life_2 import Solution as Solution2
from game_of_life_3 import Solution as Solution3

from copy import deepcopy

from testcases import TestCases


class Testing(unittest.TestCase):
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.method_count = 3

    def which_method_to_test(self, which, y) -> int:
        """
        Handles testing multiple implementations of a given method.

        Args:
            `which`: Which method to test.
            `x`: A first input into the given method to test.
        """
        x = deepcopy(y)

        # Collection of solutions
        if which == 1:
            Solution().game_of_life(x)
            return x
        elif which == 2:
            Solution2().game_of_life_2(x)
            return x
        elif which == 3:
            Solution3().game_of_life_3(x)
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

    def test_6(self):
        """Test 6"""
        which_test = TestCases.test_6
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

    def test_7(self):
        """Test 7"""
        which_test = TestCases.test_7
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

    def test_8(self):
        """Test 8"""
        which_test = TestCases.test_8
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

    def test_9(self):
        """Test 9"""
        which_test = TestCases.test_9
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

    def test_10(self):
        """Test 10"""
        which_test = TestCases.test_10
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
