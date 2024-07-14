"""Module for performing unit-tests on my functions"""

import unittest
from minimum_genetic_mutation import Solution
from minimum_genetic_mutation_2 import Solution as Solution2
from minimum_genetic_mutation_3 import Solution as Solution3

from testcases import TestCases


class Testing(unittest.TestCase):
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.method_count = 3

    def which_method_to_test(self, which, x, y, z) -> int:
        """
        Handles testing multiple implementations of a given method.

        Args:
            `which`: Which method to test.
            `x`: A first input into the given method to test.
            `y`: A second input.
            `z`: A third input.
        """

        # Collection of solutions
        if which == 1:
            s = Solution()
            return s.min_mutation(x, y, z)
        elif which == 2:
            t = Solution2()
            return t.min_mutation_2(x, y, z)
        elif which == 3:
            u = Solution3()
            return u.min_mutation_3(x, y, z)

    def test_1(self):
        """Test 1"""
        which_test = TestCases.test_1
        test_start = which_test[0]
        test_end = which_test[1]
        test_list = which_test[2]
        correct = which_test[3]
        test_description = which_test[4]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_start, test_end, test_list)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_2(self):
        """Test 2"""
        which_test = TestCases.test_2
        test_start = which_test[0]
        test_end = which_test[1]
        test_list = which_test[2]
        correct = which_test[3]
        test_description = which_test[4]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_start, test_end, test_list)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_3(self):
        """Test 3"""
        which_test = TestCases.test_3
        test_start = which_test[0]
        test_end = which_test[1]
        test_list = which_test[2]
        correct = which_test[3]
        test_description = which_test[4]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_start, test_end, test_list)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_4(self):
        """Test 4"""
        which_test = TestCases.test_4
        test_start = which_test[0]
        test_end = which_test[1]
        test_list = which_test[2]
        correct = which_test[3]
        test_description = which_test[4]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_start, test_end, test_list)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_5(self):
        """Test 5"""
        which_test = TestCases.test_5
        test_start = which_test[0]
        test_end = which_test[1]
        test_list = which_test[2]
        correct = which_test[3]
        test_description = which_test[4]
        for w in range(1, self.method_count + 1):
            result = self.which_method_to_test(w, test_start, test_end, test_list)
            self.assertEqual(
                result,
                correct,
                "Which method: " + str(w) + " - " + test_description,
            )
