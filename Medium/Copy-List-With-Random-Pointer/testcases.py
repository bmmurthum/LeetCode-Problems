"""A collection of test cases and solutions for `copy_list_with_random_pointer.py` tests."""

from node import Node


class TestCases:
    """
    A collection of test cases and solutions for `copy_list_with_random_pointer.py` tests.
    """

    # How to validate this?

    test_string = "Case: Example 1."
    a = Node(7)
    b = Node(13)
    c = Node(11)
    d = Node(10)
    e = Node(1)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    b.random = a
    c.random = e
    d.random = c
    e.random = a
    test_input = a
    test_1 = [test_input, test_string]

    test_string = "Case: Example 2."
    a = Node(1)
    b = Node(2)
    a.next = b
    a.random = b
    b.random = b
    test_input = a
    test_2 = [test_input, test_string]

    test_string = "Case: Example 3."
    a = Node(3)
    b = Node(3)
    c = Node(3)
    a.next = b
    b.next = c
    b.random = a
    test_input = a
    test_3 = [test_input, test_string]

    test_string = "Case: All randoms are None."
    a = Node(3)
    b = Node(3)
    c = Node(3)
    a.next = b
    b.next = c
    test_input = a
    test_4 = [test_input, test_string]

    test_string = "Case: All randoms are first node."
    a = Node(-4)
    b = Node(-5)
    c = Node(-7)
    a.next = b
    b.next = c
    a.random = a
    b.random = a
    c.random = a
    test_input = a
    test_5 = [test_input, test_string]

    test_string = "Case: No nodes."
    a = None
    test_input = a
    test_6 = [test_input, test_string]

    test_string = "Case: 15 nodes."
    a = Node(7)
    b = Node(13)
    c = Node(11)
    d = Node(10)
    e = Node(1)
    f = Node(7)
    g = Node(13)
    h = Node(11)
    i = Node(10)
    j = Node(1)
    k = Node(7)
    l = Node(13)
    m = Node(11)
    n = Node(10)
    o = Node(1)
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
    l.next = m
    m.next = n
    n.next = o
    a.random = a
    c.random = e
    d.random = b
    e.random = n
    f.random = m
    g.random = o
    h.random = n
    n.random = d
    test_input = a
    test_7 = [test_input, test_string]

    test_string = "Case: Single node."
    a = Node(2)
    test_input = a
    test_8 = [test_input, test_string]

    test_string = "Case: Single node, random on itself."
    a = Node(2)
    a.random = a
    test_input = a
    test_9 = [test_input, test_string]

    test_string = "Case: Two nodes."
    a = Node(1)
    b = Node(4)
    a.next = b
    a.random = b
    test_input = a
    test_10 = [test_input, test_string]
