"""Module for performing unit-tests on my functions"""

import unittest
from rotate_list import Solution


class ListNode:
    """Given class by LeetCode to manipulate linked-links"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.sol = Solution()
        self.method_count = 2

    def which_method_to_test(self, i, x, y):
        """Decide which variation method to test"""
        if i == 1:
            return self.sol.rotate_right_1(x, y)
        elif i == 2:
            return self.sol.rotate_right_2(x, y)

    def test_simple_1(self):
        """Testing simple case"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(1, ListNode(2, ListNode(3, None)))
            rotation = 2
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "2 3 1"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )

    def test_length_zero(self):
        """Testing zero length of node list"""
        for w in range(1, self.method_count + 1):
            linked_list = None
            rotation = 2
            result = self.which_method_to_test(w, linked_list, rotation)
            self.assertEqual(
                result is None,
                True,
                "The result is incorrect on simple case.",
            )

    def test_length_one(self):
        """Testing node list of length 1"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(6, None)
            rotation = 8
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "6"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )

    def test_rotation_zero(self):
        """Testing rotation 0"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(1, ListNode(2, ListNode(3, None)))
            rotation = 0
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 2 3"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )

    def test_rotation_one(self):
        """Testing rotation 1"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(1, ListNode(2, ListNode(3, None)))
            rotation = 1
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "3 1 2"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )

    def test_rotation_same_as_length(self):
        """Testing node list of length 1"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(1, ListNode(2, ListNode(3, None)))
            rotation = 3
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 2 3"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )

    def test_rotation_same_as_length_2(self):
        """Testing node list of length 1"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(1, ListNode(2, None))
            rotation = 2
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 2"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )

    def test_rotation_less_than_length(self):
        """Testing rotation less than length"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
            )
            rotation = 3
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "3 4 5 1 2"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )

    def test_rotation_more_than_length(self):
        """Testing rotation more than length"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
            )
            rotation = 6
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "5 1 2 3 4"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )

    def test_rotation_more_than_length_and_divisible_by(self):
        """Testing rotation more than length, and len%rot==0"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
            )
            rotation = 10
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 2 3 4 5"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )

    def test_rotation_more_than_length_more(self):
        """Testing rotation more than length by many"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
            )
            rotation = 23
            result = self.which_method_to_test(w, linked_list, rotation)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "3 4 5 1 2"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on simple case.",
            )


if __name__ == "__main__":
    unittest.main()
