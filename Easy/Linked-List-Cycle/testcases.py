"""A collection of test cases and solutions for `linked_list_cycle.py` tests."""


class ListNode:
    """Node definition given by LeetCode."""

    def __init__(self, x):
        self.val = x
        self.next = None


class TestCases:
    """
    A collection of test cases and solutions for `linked_list_cycle.py` tests.
    """

    test_string = "Case: Example 1."
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    correct = True
    test_input = a
    test_1 = [test_input, correct, test_string]

    test_string = "Case: Example 2."
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    b.next = a
    correct = True
    test_input = a
    test_2 = [test_input, correct, test_string]

    test_string = "Case: Example 3."
    a = ListNode(1)
    correct = False
    test_input = a
    test_3 = [test_input, correct, test_string]

    test_string = "Case: 5-long linked-list with cycle."
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(5)
    d = ListNode(7)
    e = ListNode(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = b
    correct = True
    test_input = a
    test_4 = [test_input, correct, test_string]

    test_string = "Case: 12-long linked-list without cycle."
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(5)
    d = ListNode(7)
    e = ListNode(7)
    f = ListNode(7)
    g = ListNode(1)
    h = ListNode(-1)
    i = ListNode(-203)
    j = ListNode(24)
    k = ListNode(2)
    l = ListNode(8)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    h.next = i
    i.next = j
    j.next = k
    k.next = l
    l.next = None
    correct = False
    test_input = a
    test_5 = [test_input, correct, test_string]

    test_string = "Case: 12-long linked-list with cycle."
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(5)
    d = ListNode(7)
    e = ListNode(7)
    f = ListNode(7)
    g = ListNode(1)
    h = ListNode(-1)
    i = ListNode(-203)
    j = ListNode(24)
    k = ListNode(2)
    l = ListNode(8)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    h.next = i
    i.next = j
    j.next = k
    k.next = l
    l.next = a
    correct = True
    test_input = a
    test_6 = [test_input, correct, test_string]

    test_string = "Case: Single item, cycle."
    a = ListNode(1)
    a.next = a
    correct = True
    test_input = a
    test_7 = [test_input, correct, test_string]

    test_string = "Case: Single item, no cycle."
    a = ListNode(1)
    a.next = None
    correct = False
    test_input = a
    test_8 = [test_input, correct, test_string]

    test_string = "Case: No items."
    a = None
    correct = False
    test_input = a
    test_9 = [test_input, correct, test_string]
