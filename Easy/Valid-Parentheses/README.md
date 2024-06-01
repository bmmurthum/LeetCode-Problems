# Valid Parentheses

**Description:**

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


**Example:**
```
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False

Input: s = "(([][]({})))"
Output: True

Input: s = "("
Output: False

Input: s = "]]]]"
Output: False
```

## Overview

My solution iterates through the string of parentheses building and removing from a stack as we go. If the last item on the stack doesn't appropriately fit with the newly seen parentheses' type, we know that this is a false case.

There's the edge case of a single parentheses that is easily known false. We handled that right away. It's also known that any odd-length given string of parentheses would has some lingering character. We also handle that in the beginning.

We use a `deque` type stack as the [Python Library](https://docs.python.org/3/library/collections.html#collections.deque) writes that this type is optimized as thread-safe and memory efficient in a different way than a list. With a `O(1)` cost for `.append()` and `.pop()`, compared to `O(n)` of a default list. I didn't test for optimization, but in another situation I may.

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Valid-Parentheses/test.py) for this problem with `import unittest`. Tests were made for:
- Correct & incorrect simple cases
- More open brackets than closed
- Correct & incorrect cases of nested brackets
- Incorrect single bracket case
- Incorrect all open/closed bracket case
- Incorrect check-by-odd-number case
- Incorrect case by empty stack met with close bracket

## Reflections

On submission, I was given an error on the case of `s = "(){}}{"`. I ran the code step by step on Visual Studio Code's debugger to see that the pointer I was using was set to `-1` at a point to call for a read from the stack. At the point in which we'd call from the stack that's empty, it's known that the method should return `False`, so we implemented that, and added case that to the test suite.