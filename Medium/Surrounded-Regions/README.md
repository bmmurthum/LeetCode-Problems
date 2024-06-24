# Number of Islands

**Description:**

You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`, capture regions that are **surrounded**:

- **Connect:** A cell is connected to adjacent cells horizontally or vertically.
- **Region:** To form a region connect every 'O' cell.
- **Surround:** The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all `'O'`s with `'X'`s in the input matrix `board`.

**Example:**

```text
Input: board = 
  [["X","X","X","X"],
   ["X","O","O","X"],
   ["X","X","O","X"],
   ["X","O","X","X"]]

Output: 
  [["X","X","X","X"],
   ["X","X","X","X"],
   ["X","X","X","X"],
   ["X","O","X","X"]]
```

## Overview

Our solution iterates once over the 2D list `board` to find any `"O"` items that could be "regions" that need to have a "surround" applied. This search ignores the edges, because anything at that position will not possibly be surrounded.

Once it finds any `"O"` within the search, we use a recursive depth-first-search `mark_connected()` on that position to look for any connected pieces. Any connected pieces are marked temporarily with `"T"`, then if we find that it should be surrounded, because no piece touches an edge, we replace all the `"T"`s with `"X"` to apply the "surround".

If `mark_connected()` does find an edge, all pieces that are confirmed to stay `"O"` after our full run are marked `"Q"` to be ignored while we search for more `"O"` on the `board`.

We try to minimize iteration through the `board` while inside `mark_connected()` by keeping track of the total area that encapsulates the "region" that we're looking at, with `min_x`, `max_x` and the rest. We update only this area upon this completion.

We handle edge cases that wouldn't possibly have a "surround" with the following:

```python
width = len(board[0])
height = len(board)
if width <= 2 or height <= 2:
            return
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and confidence in robustness.

We ran this for my solution and two other's solutions.

We checked for:

- LeetCode's example case
- Single item on the `board`, both `"X"` and `"O"`
- 2 x 6 array, which couldn't have a surround
- 4 x 2 array, which couldn't have a surround
- No surrounds
- Regions only on edges
- No regions
- Middle area is all region, to be surrounded
- Small strips of regions
- All region
- A false correct solution to assert a false case

### Code Coverage

We received 100% code coverage on my method from the unit-test using the `coverage.py` tool.

In `other_solution_2.py`, line 20, their checking for a given `grid` as a `None` is unused. This is given in the constraints of the problem as never going to happen, and could be deleted from their solution.

```PowerShell
> coverage run unit_test.py
> coverage html
> coverage report -m 
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
number_of_islands.py      36      0   100%
other_solution_1.py       21      0   100%
other_solution_2.py       19      1    95%   20
test_cases.py             45      0   100%
unit_test.py             111      0   100%
----------------------------------------------------
TOTAL                    232      1    99%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution `solve_1()` and two other people's solutions `solve_2()` and `solve_3()`.

This is tested with `test_11` of a mix of smaller regions.

Memory blocks used:

- `solve_1()`: 1648 blocks
- `solve_2()`: 4776 blocks
- `solve_3()`: 432 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on two different test cases. This shows that my optimization  for less `board` list updates on cases of smaller regions reveals itself, if not in every case.

**Test 11:** A case of many smaller regions.

- `solve_1()`: 1.053 x 10^-5 sec
- `solve_2()`: 1.880 x 10^-5 sec
- `solve_3()`: 1.202 x 10^-5 sec

**Test 6:** No surrounded regions.

- `solve_1()`: 1.097 x 10^-5 sec
- `solve_2()`: 1.471 x 10^-5 sec
- `solve_3()`: 0.897 x 10^-5 sec

## Reflections

Thinking about balancing where to design more calls--trying to avoid iterating over the 2D list many times--was a real brain squeezer.

I'm not too happy with how bloated my solution reads. I put the `mark_connected()` function within `solve_1()` for the sake of information hiding exercise, as if its a private method to this class.

## Solution Variations

### other_solution_2.py

This solution, more than any I've seen in a while, does a heavy use of instance variables `self.grid` `self.ROWS` as well as use of a static method that doesn't have access to the instance variables. I searched to see if static methods are more optimized and couldn't find anything on that, just that Python is slow generally and we shouldn't care too much for optimization.

They're really using the full range of options in syntax, with constants as `COLS` and `__X`, and assigning variables in the list format a lot `x,y,z = 1,2,3`.

Their renaming of the initial `board` to `grid` created a new copy of the list, just for the rename. And then again with `self.grid = grid`. And then another list of the same size of booleans `self.visited`.

And it's less readable than the other solution.

```python
class Solution:
    __X = "X"
    __O = "O"
    

    def __init__(self):
        self.grid, self.ROWS, self.COLS, self.visited = None, None, None, None
        self.banned = set()

    def in_range(self, i, j):
        return 0 <= i < self.ROWS and 0 <= j < self.COLS

    @staticmethod
    def get_neighbors(i, j):
        return ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))

    def dfs(self, i, j):
        if (
            not self.in_range(i, j)
            or self.visited[i][j]
            or not self.grid[i][j] == self.__O
        ):
            return

        self.visited[i][j] = True
        self.banned.add((i, j))

        for x, y in self.get_neighbors(i, j):
            self.dfs(x, y)

    def solve_2(self, board: list[list[str]]) -> None:
        grid = board
        self.grid, self.ROWS, self.COLS = grid, len(grid), len(grid[0])
        self.visited = [[False] * self.COLS for _ in range(self.ROWS)]

        corners = []

        for i in range(1, self.ROWS - 1):
            if self.grid[i][0] == self.__O:
                corners.append((i, 0))
            if 0 < self.COLS - 1 and self.grid[i][self.COLS - 1] == self.__O:
                corners.append((i, self.COLS - 1))

        for j in range(self.COLS):
            if self.grid[0][j] == self.__O:
                corners.append((0, j))
            if 0 < self.ROWS - 1 and self.grid[self.ROWS - 1][j] == self.__O:
                corners.append((self.ROWS - 1, j))

        for i, j in corners:
            self.dfs(i, j)

        self.banned = self.banned.difference(set(corners))

        for i in range(1, self.ROWS - 1):
            for j in range(1, self.COLS - 1):
                if (i, j) not in self.banned:
                    self.grid[i][j] = self.__X

        return self.grid
```

### other_solution_3.py

I like their idea of starting at the edges to find staying regions.

Their `dfs()` is clean. If this is an `"O"` make it a `"#"`, do this to the neighbors.

```python
class Solution:
    def solve_3(self, board: list[list[str]]) -> None:
        for i in range(len(board)):
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            if board[i][len(board[0]) - 1] == "O":
                self.dfs(board, i, len(board[0]) - 1)
        for j in range(len(board[0])):
            if board[0][j] == "O":
                self.dfs(board, 0, j)
            if board[len(board) - 1][j] == "O":
                self.dfs(board, len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"

    def dfs(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == "O":
            board[i][j] = "#"
            self.dfs(board, i + 1, j)
            self.dfs(board, i - 1, j)
            self.dfs(board, i, j + 1)
            self.dfs(board, i, j - 1)
```
