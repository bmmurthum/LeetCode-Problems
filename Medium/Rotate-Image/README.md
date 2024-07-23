# Rotate Image

**Description:**

You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

**Constraints:**

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

**Examples:**

```text
Input: 
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

Output:  [[7,4,1],
          [8,5,2],
          [9,6,3]]

Input: 
matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]

Output:  [[15,13,2,5],
          [14,3,4,1],
          [12,6,8,9],
          [16,7,10,11]]
```

## Overview

My solution looks at the top left quadrant of the matrix. For each item in that section, we rotate that value to its correct position and its replacement to the next.

The quadrant has a different shape for odd-numbered matrix width, so we handle that differently.

This is a third iteration on a solution to this problem, it's less readable than my first solution but over twice as fast.

```python
class Solution:
    """Problem given by LeetCode."""
    def rotate_c(self, matrix: list[list[int]]) -> None:
        """
        Modifies a given matrix in-place to have all the values be 'rotated' 90
        degrees in their positions.

        Args:
            `matrix`: The given 2D list to be modified.
        Returns:
            `None`
        """

        width = len(matrix)
        if width == 1:
            return
        y_range = width // 2
        if width % 2 == 1:
            y_range = (width // 2) + 1
        for x in range(width // 2):
            for y in range(y_range):
                value = matrix[y][x]
                matrix[y][x] = matrix[width - 1 - x][y]
                matrix[width - 1 - x][y] = matrix[width - 1 - y][width - 1 - x]
                matrix[width - 1 - y][width - 1 - x] = matrix[x][width - 1 - y]
                matrix[x][width - 1 - y] = value
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and general confidence.

We ran this for my three solutions and two other people's solutions.

We checked for:

- LeetCode's two example cases.
- A matrix width of 1, 2 and 5
- A matrix with all the same values

### Code Coverage

We received 100% code coverage on my methods from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run -m unittest
> coverage report
Name                Stmts   Miss  Cover
---------------------------------------
rotate_image.py        72      0   100%
rotate_image_2.py      13      0   100%
rotate_image_3.py       7      0   100%
test_unittests.py      67      0   100%
testcases.py           25      0   100%
---------------------------------------
TOTAL                 184      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solutions `rotate()` `rotate_b()` and `rotate_c()` against the other solutions `rotate_2()` and `rotate_3()`.

**Test 2:** LeetCode's 4x4 matrix example.

Memory blocks used:

- `rotate()`: 864 blocks
- `rotate_b()`: 424 blocks
- `rotate_c()`: 416 blocks
- `rotate_2()`: 400 blocks
- `rotate_3()`: 432 blocks

**Test 5:** A 5x5 matrix example.

Memory blocks used:

- `rotate()`: 688 blocks
- `rotate_b()`: 400 blocks
- `rotate_c()`: 392 blocks
- `rotate_2()`: 392 blocks
- `rotate_3()`: 424 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on a test cases.

**Test 2:** LeetCode's 4x4 matrix example.

- `rotate()`: 1.390 x 10^-6 sec
- `rotate_b()`: 0.958 x 10^-6 sec
- `rotate_c()`: 0.921 x 10^-6 sec
- `rotate_2()`: 0.851 x 10^-6 sec
- `rotate_3()`: 0.866 x 10^-6 sec

**Test 5:** A 5x5 matrix example.

- `rotate()`: 1.877 x 10^-6 sec
- `rotate_b()`: 1.389 x 10^-6 sec
- `rotate_c()`: 1.344 x 10^-6 sec
- `rotate_2()`: 1.072 x 10^-6 sec
- `rotate_3()`: 1.111 x 10^-6 sec

## Reflections

Looking at my progression of solutions and the collection of others', this problem seems to call for solutions that are less comprehensible when they become more efficient. I'd suggest leaving more notes in the code when doing some of this sort of refactoring.

## Solution Variations

### rotate_image_2.py

This is the fastest solution, but I don't understand how this person came to this algorithm featuring a shrinking `l` and `r`.

```python
class Solution:
    def rotate_2(self, matrix: list[list[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1
```

### rotate_image_3.py

I do not see the appeal of a `matrix.reverse()` here. Looks like some origami-type gymnastic move.

```python
class Solution:
    def rotate_3(self, matrix: list[list[int]]) -> None:
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```
