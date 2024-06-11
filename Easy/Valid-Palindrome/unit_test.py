"""Module for performing unit-tests on my functions"""

import unittest
from valid_palindrome import Solution


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.sol = Solution()

    def test_simple_with_spaces(self):
        """Testing simple case"""
        s = "race a car"
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, False, "The result is incorrect on simple case.")

    def test_with_grammar(self):
        """Testing simple case"""
        s = "A man, a plan, a canal: Panama"
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, True, "The result is incorrect on simple case.")

    def test_only_space(self):
        """Testing simple case"""
        s = " "
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, True, "The result is incorrect on simple case.")

    def test_all_nonalphanum(self):
        """Testing simple case"""
        s = "[[***&&&&"
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, True, "The result is incorrect on simple case.")

    def test_one_letter(self):
        """Testing simple case"""
        s = "a"
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, True, "The result is incorrect on simple case.")

    def test_upper_and_lowercase(self):
        """Testing simple case"""
        s = "aBba"
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, True, "The result is incorrect on simple case.")

    def test_numbers_and_odd_length(self):
        """Testing simple case"""
        s = "1234321"
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, True, "The result is incorrect on simple case.")

    def test_false_case_1(self):
        """Testing simple case"""
        s = "123221"
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, False, "The result is incorrect on simple case.")

    def test_false_case_2(self):
        """Testing simple case"""
        s = "1234565432"
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, False, "The result is incorrect on simple case.")

    def test_false_case_3(self):
        """Testing simple case"""
        s = "123456788889888888754321"
        result = self.sol.is_palindrome_1(s)
        self.assertEqual(result, False, "The result is incorrect on simple case.")


if __name__ == "__main__":
    unittest.main()
