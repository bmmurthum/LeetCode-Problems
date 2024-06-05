# Min Stack

**Description:**

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

```python3
class MinStack:

    def __init__(self):
        
    def push(self, val: int) -> None:
        
    def pop(self) -> None:
        
    def top(self) -> int:

```

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element val onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.
- You must implement a solution with `O(1)` time complexity for each function.


**Example:**
```
Input:  ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],        [-2],  [0],   [-3],  [],      [],   [],   []]

Output: [null,      null,  null,  null,  -3,      null,  0,   -2]
```


## Overview

My solution builds a `stack` with a simple Python list inside the object alongside a pointer to the end value's index. Using this to `pop()` and `push()` by removing/adding a last element from the list and moving the pointer accordingly.

The current minimum value is stored and it's index in the `stack` list as stand alone variables. A parallel list `minIndexList` is made and destroyed that keeps a record of the last known minimum value's `index`. These serve as pointers to the values in `stack`.

```
stack = []
3  4  5  1  2 -1 -2  3
minIndexList = []
0  0  0  0  3  3  5  5
```

When a `pop()` removes the known minimum value, we update the new minimum value to the value that this item points to.

We made an effort to not use Python's own `pop()` `push()` and `min()` methods, as this seems an exercise of creating these.

On the given constrain of making these stack functions `O(1)` time, we avoided any iteration through the list by using the list of pointers and stored values. We also avoided Python's `min()` for this reason. `min()` would have to iterated through the list everytime we'd want that info.

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/Min-Stack/test.py) for this problem with `import unittest`. Tests were made for:
- A simple collection
- All zeroes
- Minimum value at the end
- Minimum value one before end
- Minimum in beginning with `pop()`
- Descending list with and without `pop()`
- Ascending list with and without `pop()`
- `pop()` down to one value
- `pop()` down to no stack, then adding values back in
