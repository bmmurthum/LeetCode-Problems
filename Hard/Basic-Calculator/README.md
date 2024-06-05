# Basic Calculator

**Description:**

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

**Example:**
```
Input: s = "1 + 1"
Output: 2

Input: s = " 2-1 + 2 "
Output: 3

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## Overview

First, we clean up the string's spaces.
```python3
while s != s.replace(" ",""):
    s = s.replace(" ","")
    stack = []
```

Then, our program transforms the given `string` into a list of characters and integers. `"1+2"` becomes `[1,"+",2]`.
```python3
for char in s:
    if char == "(" or char == ")" or char == "+" or char == "-":
        stack.append(char)
    else:
        stack.append(int(char))
```

Then we make sure neighboring integers are considered as part of a larger integer. `[1,2,"+",3]` becomes `[12,"+",3]`.
```python3
stack.append(" ")
stackLength = len(stack)
i = 0
while i < stackLength:
    while isinstance(stack[i], int) and isinstance(stack[i+1], int):
        stack[i] = int(str(stack[i])+str(stack[i+1]))
        del stack[i+1]
        stackLength -= 1
    i += 1
stack.pop()
```

Then we correctly apply the `"-"` to integers and parentheses. It's given to us that we have to accept `-(1+2)` as a unary case of `"-"`, so this becomes `-1 * (1+2)` in our program. This section also applies `"-"` in front of an integer to its following integer. `["-",1,"+",2]` becomes `[-1,"+",2]`.

After this prep work we get to the stack operating section of handling nested parentheses. The basic rundown is this:
- As we iterate through our prepped list, we keep track of the last-seen `"("` in the stack `lastOpenList`, which pairs in length with our `newStack` stack.
- To iterate, we push `append()` a value onto the stack `newStack` if it's not `")"`.
- When we reach a `")"`, we start iterating through the `newStack` adding and subtracting as we go. We remove values from this stack as we do the adding and subtracting.
- At the conclusion of a full `"(1+2)"` we replace this with it's appropriate integer `"3"`.
  - If this parentheses section was preceded with a `"-"` as `"(-(1+2))"` the replacement is multiplied by negative one.

After the handling of the parentheses, we do a iteration though the remaining addition and substraction for a total.

## Tests

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Hard/Basic-Calculator/test.py) for this problem with `import unittest`. Tests were made for:
- More and less spaces in initial string
- Simple addition
- All subtraction
- No parentheses
- `"-"` at beginning in front of `"("` and in front of an integer
- Back to back parentheses `"(1+2)+(3+4)+(5+3+1)"`
- Nested parentheses `"-(1-(2-(3-4)))"`
- Unary `"-"` near parenthese `"-(3-(-(4+5)))"`


## Reflections

The requirements weren't clear on if I needed to handle integers of multiple digits in the initial given string. I'm not sure I needed to catch that case.

I explored variation of a more standard `stack` approach, but the nature of the `"-"` having directional application suggested I apply the math left-to-right, at least within the parentheses. I imagine there's a more efficient way of handling this, either with iterating the initial string directly, or in using less calls to memory with different storing of the "last seen open parenthesis".

The `unary` operation of `"-"` was trouble. Trying to figure the logic where that character should be handled differently took some time.

I ran into some cases of the length of the `lastOpenList` list not following the `newStack` list. This prompted some debug work with break points to see what was happening. 