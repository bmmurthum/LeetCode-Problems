"""Module for performing unit-tests on my functions"""

import unittest
from reverse_words_in_a_string import Solution


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.sol = Solution()

    def test_simple_1(self):
        """Testing simple case"""
        s = "the sky is blue"
        correct_solution = "blue is sky the"
        result = self.sol.reversewords_2(s)
        self.assertEqual(
            result, correct_solution, "The result is incorrect on simple case."
        )

    def test_endspaces(self):
        """Testing end-spaces case"""
        s = "     hello world   "
        correct_solution = "world hello"
        result = self.sol.reversewords_2(s)
        self.assertEqual(
            result, correct_solution, "The result is incorrect on end-spaces case."
        )

    def test_internalspaces(self):
        """Testing internal-spaces case"""
        s = "whats     your  name"
        correct_solution = "name your whats"
        result = self.sol.reversewords_2(s)
        self.assertEqual(
            result, correct_solution, "The result is incorrect on internal-spaces case."
        )

    def test_numbers(self):
        """Testing numbers inside string"""
        s = "we made 5 total cakes"
        correct_solution = "cakes total 5 made we"
        result = self.sol.reversewords_2(s)
        self.assertEqual(
            result, correct_solution, "The result is incorrect on internal-spaces case."
        )


if __name__ == "__main__":
    unittest.main()
