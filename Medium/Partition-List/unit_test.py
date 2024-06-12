"""Module for performing unit-tests on my functions"""

import unittest
from partition_list import Solution

# pylint: disable=W0622


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
        self.method_count = 3

    def which_method_to_test(self, i, x, y):
        """Decide which variation method to test"""
        if i == 1:
            return self.sol.partition_1(x, y)
        elif i == 2:
            return self.sol.partition_2(x, y)
        elif i == 3:
            return self.sol.partition_3(x, y)

    def test_example(self):
        """Testing example case"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2, None)))))
            )
            y = 3
            result = self.which_method_to_test(w, linked_list, y)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 2 2 4 3 5"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on example case.",
            )

    def test_two_item(self):
        """Testing two items in wrong order"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(2, ListNode(1, None))
            y = 2
            result = self.which_method_to_test(w, linked_list, y)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 2"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on two items in wrong order.",
            )

    def test_two_item_already_correct(self):
        """Testing two items that are already in correct order"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(1, ListNode(2, None))
            y = 2
            result = self.which_method_to_test(w, linked_list, y)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 2"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on two items in correct order.",
            )

    def test_items_all_above(self):
        """Testing items all being above `x` value"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                5, ListNode(4, ListNode(6, ListNode(4, ListNode(4, ListNode(9, None)))))
            )
            y = 3
            result = self.which_method_to_test(w, linked_list, y)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "5 4 6 4 4 9"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on all item values above `x` value.",
            )

    def test_items_all_below(self):
        """Testing items all being below `x` value"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                1,
                ListNode(0, ListNode(-2, ListNode(1, ListNode(3, ListNode(2, None))))),
            )
            y = 5
            result = self.which_method_to_test(w, linked_list, y)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 0 -2 1 3 2"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on all item values below `x` value.",
            )

    def test_items_same(self):
        """Testing items with same value and `x` value"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                1,
                ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, None))))),
            )
            y = 1
            result = self.which_method_to_test(w, linked_list, y)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 1 1 1 1 1"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on all items with same value and `x` value.",
            )

    def test_all_negative(self):
        """Testing items all negative"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                -1,
                ListNode(
                    -42, ListNode(-10, ListNode(-2, ListNode(-2, ListNode(-33, None))))
                ),
            )
            y = 1
            result = self.which_method_to_test(w, linked_list, y)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "-1 -42 -10 -2 -2 -33"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on all items negative.",
            )

    def test_head_is_none(self):
        """Testing ititial head being none"""
        for w in range(1, self.method_count + 1):
            linked_list = None
            y = 3
            result = self.which_method_to_test(w, linked_list, y)
            self.assertEqual(
                result,
                None,
                "The result is incorrect on head == None.",
            )

    def test_one_item(self):
        """Testing one item in linked-list"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(2, None)
            y = 1
            result = self.which_method_to_test(w, linked_list, y)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "2"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on one item in linked-list.",
            )

    def test_one_item_in_first_partition(self):
        """Testing one item in first partition"""
        for w in range(1, self.method_count + 1):
            linked_list = ListNode(
                1,
                ListNode(4, ListNode(5, ListNode(8, ListNode(7, ListNode(7, None))))),
            )
            y = 2
            result = self.which_method_to_test(w, linked_list, y)
            result_string = ""
            while result is not None:
                result_string += str(result.val) + " "
                result = result.next
            result_string = result_string.strip()
            correct_solution = "1 4 5 8 7 7"
            self.assertEqual(
                result_string,
                correct_solution,
                "The result is incorrect on one item first partition.",
            )


if __name__ == "__main__":
    unittest.main()
