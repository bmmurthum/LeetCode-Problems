# Set Matrix Zeroes

**Description:**

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it `in-place`.

**Constraints:**

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-231 <= matrix[i][j] <= 231 - 1`

**Examples:**

```text
Input: matrix = 
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output: 
[[1,0,1],
 [0,0,0],
 [1,0,1]]

Input: matrix = 
[[0,1,2,0],
 [3,4,5,2],
 [1,3,1,5]]
Output: 
[[0,0,0,0],
 [0,4,5,0],
 [0,3,1,0]]
```

## Overview

My solution aims at solving the problem with a O(1) space constraint. We largely use the given memory of the 2D list `matrix` to do algorithm manipulation.

I made two solutions to this problem, we'll look at our second solution `set_zeroes_b()`. Both solutions use only the memory of the given list to do manipulations. Our second one means to do less updating of `matrix`.

In this solution:

1. We use the top row and left column to record (with `"#"`) if there was a zero found in that row or column.
2. Handle changes of values by looking at the top row.
    - If there's a `"#"` we change the values of that column to `0`.
    - If there's a `0`, we change values of this top row to have `"*"` and also change the column values to `0`.
3. Handle changes of values by looking at left column, similarly.
4. Handle the top left corner value.
5. Clean up last `"*"` values.

```python
class Solution:
    """Problem given by LeetCode."""
    def set_zeroes_b(self, matrix: list[list[int]]) -> None:
    """
    Modifies a given matrix in-place to have values in a row or col
    containing a zero all be now set to zero. Modifies in-place.

    Args:
        `matrix`: The given 2D list to be modified.
    Returns:
        `None`
    """

    width = len(matrix[0])
    height = len(matrix)

    # Handle marking which rows and cols to change later
    for x in range(width):
        for y in range(height):
            if matrix[y][x] == 0:
                if matrix[0][x] != 0:
                    matrix[0][x] = "#"
                if matrix[y][0] != 0:
                    matrix[y][0] = "#"
    # Handle cols
    for x in range(1, width):
        if matrix[0][x] == 0:
            for i in range(width):
                if matrix[0][i] != 0 and matrix[0][i] != "#":
                    matrix[0][i] = "*"
            for i in range(height):
                matrix[i][x] = 0
        if matrix[0][x] == "#":
            for i in range(height):
                matrix[i][x] = 0
    # Handle rows
    for y in range(1, height):
        if matrix[y][0] == 0:
            for i in range(height):
                if matrix[i][0] != 0 and matrix[i][0] != "#":
                    matrix[i][0] = "*"
            for i in range(width):
                matrix[y][i] = 0
        if matrix[y][0] == "#":
            for i in range(width):
                matrix[y][i] = 0
    # Clean top left corner
    if matrix[0][0] == "#" or matrix[0][0] == "*":
        matrix[0][0] = 0
    elif matrix[0][0] == 0:
        for x in range(width):
            matrix[0][x] = 0
        for y in range(height):
            matrix[y][0] = 0
    # Clean top row
    for x in range(width):
        if matrix[0][x] == "*":
            matrix[0][x] = 0
    # Clean left column
    for y in range(height):
        if matrix[y][0] == "*":
            matrix[y][0] = 0
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and general confidence.

We ran this for my two solutions `set_zeroes` and `set_zeroes_b`, and three other people's solutions.

We checked for:

- LeetCode's two example cases.
- A matrix of all zeroes.
- A matrix with zeroes in the top row.
- A matrix with zeroes in the left column.
- No zeroes.
- Zeroes only in each corner.
- A mix of values with negative values.
- A result case in which there's one value left non-zero.
- A 150x180 dimension case.

### Code Coverage

We received 100% code coverage on my methods from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run -m unittest
> coverage report
Name                     Stmts   Miss  Cover
--------------------------------------------
set_matrix_zeroes.py        60      0   100%
set_matrix_zeroes_2.py      16      0   100%
set_matrix_zeroes_3.py      20      0   100%
set_matrix_zeroes_4.py      17      0   100%
test_unittests.py          100      0   100%
testcases.py                41      0   100%
--------------------------------------------
TOTAL                      254      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solutions against the others' solutions.

**Test 9:** Generated 150x180 case.

- `set_zeroes()`: 456 blocks
- `set_zeroes_b()`: 416 blocks
- `set_zeroes_2()`: 3176 blocks
- `set_zeroes_3()`: 3064 blocks
- `set_zeroes_4()`: 3064 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on a test cases.

**Test 9:** Generated 150x180 case.

- `set_zeroes()`: 0.201 sec
- `set_zeroes_b()`: 0.0038 sec
- `set_zeroes_2()`: 0.0018 sec
- `set_zeroes_3()`: 0.0019 sec
- `set_zeroes_4()`: 0.0019 sec

## Reflections

My better solution is about 2x slower than the other solutions. I'm ok with this in knowing that I went for the goal of using O(1) space. Each of their solutions use some variation of a new 2D list to record positions of `0`.

This is a quick illustration of how it can be valuable to use more memory to allow for faster solutions.

## Solution Variations

### set_matrix_zeroes_2.py

This is the fastest solution, using the most memory.

They use `1` and `0` instead of `True` and `False` where they could've, this may be costing them more memory than needed, however slight.

The problem calls for the solution to be done in place, this function returns the solution. If the function were called without assigning the result, it would still function as intended, but I would remove `return matrix` to align to the desires of the problem's requirements.

```python
class Solution:
    def set_zeroes_2(self, matrix: list[list[int]]) -> None:
        lr = len(matrix)
        lc = len(matrix[0])
        row = [0] * lr
        col = [0] * lc
        for i in range(lr):
            for j in range(lc):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(lr):
            for j in range(lc):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0
        return matrix
```

### set_matrix_zeroes_3.py

These last two solutions may have copied each other besides the applying of the `len(matrix)` to a variable to be used in the `range()` in iteration.

I like the verbiage of naming variables of this solution compared to `set_zeroes_4()`.

```python
class Solution:
    def set_zeroes_3(self, matrix: list[list[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        zeroCol = [False] * COLS
        zeroRow = [False] * (ROWS)
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeroCol[c] = True
                    zeroRow[r] = True
        for r in range(ROWS):
            if zeroRow[r]:
                for c in range(COLS):
                    matrix[r][c] = 0
        for c in range(COLS):
            if zeroCol[c]:
                for r in range(ROWS):
                    matrix[r][c] = 0
        return
```

### set_matrix_zeroes_4.py

```python
class Solution:
    def set_zeroes_4(self, a: list[list[int]]) -> None:
        b = [False] * len(a)
        c = [False] * len(a[0])
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 0:
                    b[i] = True
                    c[j] = True
        for i in range(len(b)):
            if b[i]:
                for j in range(len(a[0])):
                    a[i][j] = 0
        for i in range(len(c)):
            if c[i]:
                for j in range(len(a)):
                    a[j][i] = 0
```
