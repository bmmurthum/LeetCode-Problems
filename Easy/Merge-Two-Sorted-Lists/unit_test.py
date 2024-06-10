"""Module for performing unit-tests on my functions"""

import unittest
from merge_two_sorted_lists import Solution


class ListNode:
    """Defines a node object"""

    def __init__(self, val=0, next=None):  # pylint: disable=W0622
        self.val = val
        self.next = next


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.sol = Solution()

    def test_simple_1(self):
        """Testing simple case"""
        a = ListNode(0, ListNode(3, ListNode(4)))
        b = ListNode(1, ListNode(2, ListNode(6, ListNode(7))))
        a_list = [0, 3, 4]
        b_list = [1, 2, 6, 7]
        ab_list = []
        ab_list.extend(a_list)
        ab_list.extend(b_list)

        s = Solution()
        c = s.mergetwolists_1(a, b)

        in_order = True
        has_same_numbers = True
        generated_c_list = []
        while c is not None:
            if c.next is not None and c.val > c.next.val:
                in_order = False
            generated_c_list.append(c.val)
            c = c.next
        c_set = set(generated_c_list)
        for item in c_set:
            if ab_list.count(item) != generated_c_list.count(item):
                has_same_numbers = False

        self.assertEqual(
            [in_order, has_same_numbers],
            [True, True],
            "The result is incorrect on simple case.",
        )

    def test_one_empty_list(self):
        """Testing one empty list"""
        a = ListNode(1, ListNode(2, ListNode(3)))
        b = None
        a_list = [1, 2, 3]
        b_list = []
        ab_list = []
        ab_list.extend(a_list)
        ab_list.extend(b_list)

        s = Solution()
        c = s.mergetwolists_1(a, b)

        in_order = True
        has_same_numbers = True
        generated_c_list = []
        while c is not None:
            if c.next is not None and c.val > c.next.val:
                in_order = False
            generated_c_list.append(c.val)
            c = c.next
        c_set = set(generated_c_list)
        for item in c_set:
            if ab_list.count(item) != generated_c_list.count(item):
                has_same_numbers = False

        self.assertEqual(
            [in_order, has_same_numbers],
            [True, True],
            "The result is incorrect on simple case.",
        )

    def test_both_empty_list(self):
        """Testing both empty list"""
        a = None
        b = None
        a_list = []
        b_list = []
        ab_list = []
        ab_list.extend(a_list)
        ab_list.extend(b_list)

        s = Solution()
        c = s.mergetwolists_1(a, b)

        in_order = True
        has_same_numbers = True
        generated_c_list = []
        while c is not None:
            if c.next is not None and c.val > c.next.val:
                in_order = False
            generated_c_list.append(c.val)
            c = c.next
        c_set = set(generated_c_list)
        for item in c_set:
            if ab_list.count(item) != generated_c_list.count(item):
                has_same_numbers = False

        self.assertEqual(
            [in_order, has_same_numbers],
            [True, True],
            "The result is incorrect on simple case.",
        )

    def test_one_list_all_beginning(self):
        """Testing one list having all beginning small values"""
        a = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4))))))
        b = ListNode(1, ListNode(1, ListNode(1)))
        a_list = [1, 2, 3, 3, 3, 4]
        b_list = [1, 1, 1]
        ab_list = []
        ab_list.extend(a_list)
        ab_list.extend(b_list)

        s = Solution()
        c = s.mergetwolists_1(a, b)

        in_order = True
        has_same_numbers = True
        generated_c_list = []
        while c is not None:
            if c.next is not None and c.val > c.next.val:
                in_order = False
            generated_c_list.append(c.val)
            c = c.next
        c_set = set(generated_c_list)
        for item in c_set:
            if ab_list.count(item) != generated_c_list.count(item):
                has_same_numbers = False

        self.assertEqual(
            [in_order, has_same_numbers],
            [True, True],
            "The result is incorrect on simple case.",
        )

    def test_not_sorted_not_handled(self):
        """Testing output of not-sorted lists"""
        a = ListNode(1, ListNode(4, ListNode(1, ListNode(3, ListNode(3, ListNode(1))))))
        b = ListNode(5, ListNode(1, ListNode(2)))
        a_list = [1, 4, 1, 3, 3, 1]
        b_list = [5, 1, 2]
        ab_list = []
        ab_list.extend(a_list)
        ab_list.extend(b_list)

        s = Solution()
        c = s.mergetwolists_1(a, b)

        in_order = True
        has_same_numbers = True
        generated_c_list = []
        while c is not None:
            if c.next is not None and c.val > c.next.val:
                in_order = False
            generated_c_list.append(c.val)
            c = c.next
        c_set = set(generated_c_list)
        for item in c_set:
            if ab_list.count(item) != generated_c_list.count(item):
                has_same_numbers = False

        self.assertFalse(
            ([in_order, has_same_numbers] == [True, True]),
            "The result is incorrect on simple case.",
        )


if __name__ == "__main__":
    unittest.main()
