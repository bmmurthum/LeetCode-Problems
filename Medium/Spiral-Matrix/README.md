# Spiral Matrix

**Description:**

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

**Example:**

```
| 1 > 2 > 3 |
          v
| 4 > 5 | 6 |
  ^       v
| 7 < 8 < 9 |

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

| 1  >  2 >  3 >  4 |
                  v
| 5  >  6 >  7 |  8 |
  ^               v
| 9  < 10 < 11 < 12 |

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

| 1  >  2 >  3 >  4 |
                  v
| 5  >  6 >  7 |  8 |
  ^          v    v
| 9  | 10 < 11 | 12 |
  ^               v
| 13 < 14 < 15 < 16 |

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
Output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

| 1  >  2 >  3 >  4 |
Input: matrix = [[1,2,3,4]]
Output: [1,2,3,4]

| 1 |
  v
| 2 |
  v 
| 3 |
Input: matrix = [[1],[2],[3]]
Output: [1,2,3]
```

## Overview

For my solution, we imagine doing a spiral loop around the outside of the matrix to then start at a new position inside that old loop, with smaller dimensions. 

```python
# My solution
def spiral_order_1(self, matrix: list[list[int]]) -> list[int]:
    # Grabbing initial variables
    height = len(matrix)
    width = len(matrix[0])
    output_list = []
    start_x = 0
    start_y = 0
    # Do another iteration of a spiral
    while True:
        # Go right
        end_right = width - 1
        for a in range(start_x, start_x + end_right + 1):
            output_list.append(matrix[start_y][a])
        if height < 2:
            break
        # Go down
        end_down = height - 1
        for a in range(start_y + 1, start_y + end_down + 1):
            output_list.append(matrix[a][start_x + end_right])
        if width < 2:
            break
        # Go left
        end_left = width
        for a in range(1, end_left):
            output_list.append(matrix[start_y + end_down][start_x + end_right - a])
        # Go up
        end_up = height - 1
        for a in range(1, end_up):
            output_list.append(
                matrix[start_y + end_down - a][start_x + end_left - width]
            )
        # Setup for next inner spiral
        width -= 2
        height -= 2
        start_x += 1
        start_y += 1
        if width < 1:
            break
    return output_list
```

## Tests

**Unit Testing**

We implemented unit-tests for this problem with `import unittest`. We checked for:
- 3x3 matrix
- 4x4 matrix
- 3x4 matrix
- 1x3 matrix `[[1], [2], [3]]`
- 4x1 matrix `[[1, 2, 3, 4]]`
- Empty matrix `[[]]`

**Code Coverage**

We received 100% code coverage on `spiral_order_1.py` from the unit test using the `coverage.py` tool.

```
> coverage run unit_test.py
> coverage report -m 
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
spiral_matrix.py      31      0   100%
unit_test.py          38      0   100%
------------------------------------------------
TOTAL                 69      0   100%
```

**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of the function on a 4x4 case. We compare my solution with two other solutions, seen below.

Memory blocks used:

- `spiral_order_1()`: 208 blocks
- `spiral_order_2()`: 208 blocks
- `spiral_order_3()`: 896 blocks


**Process Time Testing**

I used `timeit` to isolate the individual functions on the same input.

My solution `spiral_order_1()` is 6% slower than the fastest solution `spiral_order_2()` with a 10x10 matrix case.

- `spiral_order_1()`: 7.258 x 10^-6 sec
- `spiral_order_2()`: 6.805 x 10^-6 sec
- `spiral_order_3()`: 10.80 x 10^-6 sec

## Reflections

Looking at other solutions on LeetCode, everyone is using a similar algorithm. Optimizations might be in where you place calculations within the loops. 

I could see `numpy` arrays being more efficient in some way, with the library being set up for matrix manipulations. 

With `spiral_order_3()` I trialed performance for a process of copying the given `matrix` to a numpy array to then do the algorithm. This ended up being 50% slower than my equivalent solution. The creation of a new `numpy` list always has to iterate the whole list for values, this time was not saved by the C-language and memory optimization of `numpy` when doing calculations. Potentially, if the given input/output were also `numpy` arrays, we could have better results.

## Solution Variations

`spiral_order_2()` does very similar logic. It feels more readable than mine, keeping a top `t`, bottom `b`, right `r` and left `l` that gets manipulated.

`208 memory blocks` & `6.805 x 10^-6 sec`
```python
# Someone else's solution
def spiral_order_2(self, s: str) -> bool:
    ROWS = len(matrix)
    COLS = len(matrix[0])
    l,r,t,b = 0, COLS, 0, ROWS
    res = []
    
    while l < r and t < b:
        # get all from top row
        for i in range(l,r):
            res.append(matrix[t][i])
        # once traverse top row, top is shrunk
        t += 1
        # get all right row
        for i in range(t,b):
            res.append(matrix[i][r-1]) # right is OOB
        # right is shrunk
        r -= 1
        
        if not (l < r and t < b): # pointer crossed, exit early
            break

        # get all bottom row
        for i in range(r - 1,l - 1,-1): # left is not inclusive
            res.append(matrix[b-1][i]) # bottom is OOB
        # bottom is shrunk
        b -= 1
        # get all left row
        for i in range(b - 1,t - 1,-1): #top is non inclusive
            res.append(matrix[i][l])     
        # left is shrunk
        l += 1
    return res
```

My solution, using `numpy` array for interal calculations.

`896 memory blocks` & `10.8 x 10^-6 sec`
```python
# My solution
def spiral_order_3(self, matrix: list[list[int]]) -> list[int]:
    n_arr = np.array(matrix)
    output_list = []
    height = n_arr.shape[0]
    width = n_arr.shape[1]

    start_x = 0
    start_y = 0
    while True:
        # Go right
        for a in range(start_x, start_x + width):
            output_list.append(n_arr[start_y][a])
        if height < 2:
            break
        # Go down
        for a in range(start_y + 1, start_y + height):
            output_list.append(n_arr[a][start_x + width - 1])
        if width < 2:
            break
        # Go left
        for a in range(1, width):
            output_list.append(n_arr[start_y + height - 1][start_x + width - 1 - a])
        # Go up
        for a in range(1, height - 1):
            output_list.append(n_arr[start_y + height - 1 - a][start_x])
        # Setup for next inner spiral
        width -= 2
        height -= 2
        start_x += 1
        start_y += 1
        if width < 1:
            break
    return output_list
```

