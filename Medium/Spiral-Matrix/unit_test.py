"""Module for performing unit-tests on my functions"""

import unittest
from spiral_matrix import Solution


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.sol = Solution()

    def test_simple_3by3(self):
        """Testing 3x3 case"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.sol.spiral_order_1(matrix)
        correct_solution = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(
            result, correct_solution, "The result is incorrect on simple case."
        )

    def test_4by4(self):
        """Testing 4x4 case"""
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        result = self.sol.spiral_order_1(matrix)
        correct_solution = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(
            result, correct_solution, "The result is incorrect on simple case."
        )

    def test_simple_3by4(self):
        """Testing 3x4 case"""
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        result = self.sol.spiral_order_1(matrix)
        correct_solution = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(
            result, correct_solution, "The result is incorrect on simple case."
        )

    def test_1x4(self):
        """Testing 1x4 case"""
        matrix = [[1, 2, 3, 4]]
        result = self.sol.spiral_order_1(matrix)
        correct_solution = [1, 2, 3, 4]
        self.assertEqual(
            result, correct_solution, "The result is incorrect on simple case."
        )

    def test_3x1(self):
        """Testing 1x3 case"""
        matrix = [[1], [2], [3]]
        result = self.sol.spiral_order_1(matrix)
        correct_solution = [1, 2, 3]
        self.assertEqual(
            result, correct_solution, "The result is incorrect on simple case."
        )

    def test_empty(self):
        """Testing empty case"""
        matrix = [[]]
        result = self.sol.spiral_order_1(matrix)
        correct_solution = []
        self.assertEqual(
            result, correct_solution, "The result is incorrect on simple case."
        )


if __name__ == "__main__":
    unittest.main()
