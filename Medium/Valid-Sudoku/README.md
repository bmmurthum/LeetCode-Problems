# Merge Sorted Array

**Description:**

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.


**Example:**
```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: True
```

## Overview

For the rows and columns we used a similar nested loop in which we marked a list of booleans with whether we had found each integer possible. If we find a duplicate, we return `False` to end the algorithm.

For the sub-box check we did a nested loop of `0 -> 2` in which these numbers are multipliers to our handcoded nine squares to search. These squares I added to a string to then use `str.count(7)` to check for any duplicates of integers.

## Test Cases

We ran [unit tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/Valid-Sudoku/test.py) on this problem for cases:
- Good solution
- Bad solution by row
- Bad solution by column
- Bad solution by sub-box

```
import unittest
from validSudoku import Solution
class TestMergeSortedArray(unittest.TestCase):
    def test_1(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        x = Solution.isValidSudoku(board)
        correctSolution = True
        self.assertEqual(x, correctSolution, 'Incorrect. This puzzle has no visible invalid pieces.')
```