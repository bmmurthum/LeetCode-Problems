# Evaluate Reverse Polish Notation

**Description:**

You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an `integer` that represents the value of the expression.

Note that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.


**Example:**
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```


## Overview

We see that the given input list of `int` and operations is a stack. As we iterate from the beginning to end of this given list `tokens`: 
- If the current `item` is a `int` we add it to our stack. 
- If the current `item` is an operation we run that operation on the last two items in our stack `stack[-2]` and `stack[-1]`. This new value we apply to `stack[-2]` and then pop the last value off of our stack.

The constraints given call for division cases to be truncated towards zero. For this, we observe if this result `newValue` is negative/positive, then apply `math.ceil()` or `math.floor()` appropriately. 


## Tests

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/Evaluate-Reverse-Polish-Notation/test.py) for this problem with `import unittest`. Tests were made for:
- All operations
- Negative and positive integers
- Cases of division resulting in positive/negative floats


## Reflections

At first, I tried integer division, but I ran into trouble with that. I would have liked to avoid importing any libraries. I imagine an implementation of integer division would be faster than my `newVal = stack[-2] / stack[-1]` then `newVal = int(floor(newVal))`.