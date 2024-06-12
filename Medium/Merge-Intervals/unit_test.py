"""Module for performing unit-tests on my functions"""

import unittest
from merge_intervals import Solution


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.sol = Solution()
        self.method_count = 2

    def which_method_to_test(self, i, x):
        """Decide which variation method to test"""
        if i == 1:
            return self.sol.merge_1(x)
        elif i == 2:
            return self.sol.merge_2(x)

    def test_simple_1(self):
        """Testing simple case"""
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        for w in range(1, self.method_count + 1):
            new_intervals = intervals.copy()
            result = self.which_method_to_test(w, new_intervals)
            correct_solution = [[1, 6], [8, 10], [15, 18]]
            self.assertEqual(
                result, correct_solution, "The result is incorrect on simple case."
            )

    def test_simple_2(self):
        """Testing simple case"""
        intervals = [[1, 4], [4, 5]]
        for w in range(1, self.method_count + 1):
            new_intervals = intervals.copy()
            result = self.which_method_to_test(w, new_intervals)
            correct_solution = [[1, 5]]
            self.assertEqual(
                result, correct_solution, "The result is incorrect on simple case."
            )

    def test_encapsulated_interval(self):
        """Testing encapsulated interval"""
        intervals = [[1, 4], [2, 3]]
        for w in range(1, self.method_count + 1):
            new_intervals = intervals.copy()
            result = self.which_method_to_test(w, new_intervals)
            correct_solution = [[1, 4]]
            self.assertEqual(
                result, correct_solution, "The result is incorrect on simple case."
            )

    def test_single_item(self):
        """Testing single item"""
        intervals = [[1, 2]]
        for w in range(1, self.method_count + 1):
            new_intervals = intervals.copy()
            result = self.which_method_to_test(w, new_intervals)
            correct_solution = [[1, 2]]
            self.assertEqual(
                result, correct_solution, "The result is incorrect on simple case."
            )

    def test_larger_case(self):
        """Testing single item"""
        intervals = [
            [1, 2],
            [2, 3],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 14],
            [10, 11],
            [11, 12],
            [15, 16],
            [17, 18],
            [22, 26],
        ]
        for w in range(1, self.method_count + 1):
            new_intervals = intervals.copy()
            result = self.which_method_to_test(w, new_intervals)
            correct_solution = [
                [1, 4],
                [5, 6],
                [7, 8],
                [9, 14],
                [15, 16],
                [17, 18],
                [22, 26],
            ]
            self.assertEqual(
                result, correct_solution, "The result is incorrect on simple case."
            )


if __name__ == "__main__":
    unittest.main()
