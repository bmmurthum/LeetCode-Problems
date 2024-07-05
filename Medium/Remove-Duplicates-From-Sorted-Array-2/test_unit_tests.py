"""Module for performing unit-tests on my functions"""

import unittest
import copy
from remove_duplicates_from_sorted_array_2 import Solution
from other_solution_2 import Solution as Solution2
from other_solution_3 import Solution as Solution3
from test_cases import TestCases


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

        # Test lists may be edited by the functions.
        x = copy.deepcopy(y)

        # Collection of solutions
        if which == 1:
            s = Solution()
            k = s.remove_duplicates(x)
            return k, x
        elif which == 2:
            t = Solution2()
            k = t.remove_duplicates_2(x)
            return k, x
        elif which == 3:
            u = Solution3()
            k = u.remove_duplicates_3(x)
            return k, x

    def test_1(self):
        """Test 1"""
        which_test = TestCases.test_1
        test_case = which_test[0]
        correct_list = which_test[1]
        correct_k = int(which_test[2])
        test_description = which_test[3]
        for w in range(1, self.method_count + 1):
            result, list_after = self.which_method_to_test(w, test_case)
            self.assertEqual(
                result,
                correct_k,
                "Which method: " + str(w) + " - " + test_description,
            )
            self.assertEqual(
                list_after[:correct_k],
                correct_list[:correct_k],
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_2(self):
        """Test 2"""
        which_test = TestCases.test_2
        test_case = which_test[0]
        correct_list = which_test[1]
        correct_k = int(which_test[2])
        test_description = which_test[3]
        for w in range(1, self.method_count + 1):
            result, list_after = self.which_method_to_test(w, test_case)
            self.assertEqual(
                result,
                correct_k,
                "Which method: " + str(w) + " - " + test_description,
            )
            self.assertEqual(
                list_after[:correct_k],
                correct_list[:correct_k],
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_3(self):
        """Test 3"""
        which_test = TestCases.test_3
        test_case = which_test[0]
        correct_list = which_test[1]
        correct_k = int(which_test[2])
        test_description = which_test[3]
        for w in range(1, self.method_count + 1):
            result, list_after = self.which_method_to_test(w, test_case)
            self.assertEqual(
                result,
                correct_k,
                "Which method: " + str(w) + " - " + test_description,
            )
            self.assertEqual(
                list_after[:correct_k],
                correct_list[:correct_k],
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_4(self):
        """Test 4"""
        which_test = TestCases.test_4
        test_case = which_test[0]
        correct_list = which_test[1]
        correct_k = int(which_test[2])
        test_description = which_test[3]
        for w in range(1, self.method_count + 1):
            result, list_after = self.which_method_to_test(w, test_case)
            self.assertEqual(
                result,
                correct_k,
                "Which method: " + str(w) + " - " + test_description,
            )
            self.assertEqual(
                list_after[:correct_k],
                correct_list[:correct_k],
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_5(self):
        """Test 5"""
        which_test = TestCases.test_5
        test_case = which_test[0]
        correct_list = which_test[1]
        correct_k = int(which_test[2])
        test_description = which_test[3]
        for w in range(1, self.method_count + 1):
            result, list_after = self.which_method_to_test(w, test_case)
            self.assertEqual(
                result,
                correct_k,
                "Which method: " + str(w) + " - " + test_description,
            )
            self.assertEqual(
                list_after[:correct_k],
                correct_list[:correct_k],
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_6(self):
        """Test 6"""
        which_test = TestCases.test_6
        test_case = which_test[0]
        correct_list = which_test[1]
        correct_k = int(which_test[2])
        test_description = which_test[3]
        for w in range(1, self.method_count + 1):
            result, list_after = self.which_method_to_test(w, test_case)
            self.assertEqual(
                result,
                correct_k,
                "Which method: " + str(w) + " - " + test_description,
            )
            self.assertEqual(
                list_after[:correct_k],
                correct_list[:correct_k],
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_7(self):
        """Test 7"""
        which_test = TestCases.test_7
        test_case = which_test[0]
        correct_list = which_test[1]
        correct_k = int(which_test[2])
        test_description = which_test[3]
        for w in range(1, self.method_count + 1):
            result, list_after = self.which_method_to_test(w, test_case)
            self.assertEqual(
                result,
                correct_k,
                "Which method: " + str(w) + " - " + test_description,
            )
            self.assertEqual(
                list_after[:correct_k],
                correct_list[:correct_k],
                "Which method: " + str(w) + " - " + test_description,
            )

    def test_8(self):
        """Test 8"""
        which_test = TestCases.test_8
        test_case = which_test[0]
        correct_list = which_test[1]
        correct_k = int(which_test[2])
        test_description = which_test[3]
        for w in range(1, self.method_count + 1):
            result, list_after = self.which_method_to_test(w, test_case)
            self.assertEqual(
                result,
                correct_k,
                "Which method: " + str(w) + " - " + test_description,
            )
            self.assertEqual(
                list_after[:correct_k],
                correct_list[:correct_k],
                "Which method: " + str(w) + " - " + test_description,
            )
