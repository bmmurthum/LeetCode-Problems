"""Module for performing unit-tests on my functions"""

import unittest
from minimum_number_of_arrows_to_burst_balloon import Solution


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.sol = Solution()
        self.method_count = 3

    def which_method_to_test(self, i, points):
        """Decide which variation method to test"""
        if i == 1:
            return self.sol.find_min_arrow_shots_1(points)
        elif i == 2:
            return self.sol.find_min_arrow_shots_2(points)
        else:
            return self.sol.find_min_arrow_shots_3(points)

    def test_simple_1(self):
        """Testing simple case"""
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 2
            self.assertEqual(
                result, correct_solution, "The result is incorrect on simple case."
            )

    def test_no_overlap(self):
        """Testing no overlap case"""
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 4
            self.assertEqual(
                result, correct_solution, "The result is incorrect on no overlap case."
            )

    def test_competing_overlap(self):
        """Testing competing overlap case"""
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 2
            self.assertEqual(
                result,
                correct_solution,
                "The result is incorrect on competing overlap case.",
            )

    def test_competing_overlap_diff_order(self):
        """Testing competing overlap case"""
        points = [[3, 4], [1, 2], [2, 3], [4, 5]]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 2
            self.assertEqual(
                result,
                correct_solution,
                "The result is incorrect on competing overlap case.",
            )

    def test_one_balloon(self):
        """Testing one balloon case"""
        points = [[1, 2]]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 1
            self.assertEqual(
                result,
                correct_solution,
                "The result is incorrect on one balloon case.",
            )

    def test_all_one_shot(self):
        """Testing one shot case"""
        points = [[1, 2], [1, 2], [1, 3], [2, 4]]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 1
            self.assertEqual(
                result,
                correct_solution,
                "The result is incorrect on one shot case.",
            )

    def test_all_same(self):
        """Testing one shot case"""
        points = [[1, 2], [1, 2], [1, 2]]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 1
            self.assertEqual(
                result,
                correct_solution,
                "The result is incorrect on one shot case.",
            )

    def test_shrinking_issue(self):
        """Testing shrinking issue case"""
        points = [
            [2, 3],
            [7, 15],
            [5, 12],
            [4, 5],
            [8, 13],
            [9, 16],
            [5, 8],
            [8, 16],
            [3, 4],
            [8, 17],
        ]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 3
            self.assertEqual(
                result,
                correct_solution,
                "The result is incorrect on shrinking issue case.",
            )

    def test_negative_values(self):
        """Testing negative positions case"""
        points = [[-1, 1], [0, 1], [2, 3], [1, 2]]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 2
            self.assertEqual(
                result,
                correct_solution,
                "The result is incorrect on negative positions case.",
            )

    def test_error_case(self):
        """Testing a case that gave an error case"""
        points = [
            [4289383, 51220269],
            [81692777, 96329692],
            [57747793, 81986128],
            [19885386, 69645878],
            [96516649, 186158070],
            [25202362, 75692389],
            [83368690, 85888749],
            [44897763, 112411689],
            [65180540, 105563966],
            [4089172, 7544908],
        ]
        for w in range(1, self.method_count + 1):
            new_points = points.copy()
            result = self.which_method_to_test(w, new_points)
            correct_solution = 4
            self.assertEqual(
                result,
                correct_solution,
                "The result is incorrect on negative positions case.",
            )


if __name__ == "__main__":
    unittest.main()
