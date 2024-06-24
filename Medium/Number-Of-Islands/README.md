# Number of Islands

**Description:**

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

**Example:**

```text
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Overview

My solution first looks for a x,y position of a next-land to look at with `find_next()`, then uses a depth-first search on that position with `depth_search_island()` to edit the initial list `grid` to mark where we've looked. We do this until we can't find another piece of land in the 2D list.

We use object variables `width` and `height` to avoid using `len(grid)` many times for less processing calls. We use `current_row` to aid `find_next()` in not having to look at the entire `grid` when looking for another land piece.

```python
class Solution:
    """Problem given by LeetCode."""

    def __init__(self) -> None:
        # Width and height of the 2D array, to reduce calling len() on list
        self.width = 0
        self.height = 0
        # Current row looking at for land to check on
        self.current_row = 0

    def num_islands_1(self, grid: list[list[str]]) -> int:
        """
        Looks over a given 2D array for a count of 'islands,' where an island
        is a group of `1`s with a bordering edge of `0`s. We assume that
        outside of the array is considered `0`s.

        Args:
            `grid`: A 2D array of `1` and `0`, with `1` representing land and
            `0` representing water.
        Returns:
            `count`: An integer count of number of islands.
        """

        # Grab dimensions for calls
        self.width = len(grid[0])
        self.height = len(grid)

        # Set current row to zero
        self.current_row = 0

        # Current counted islands
        island_count = 0

        while True:
            # Check for any land
            next_position = self.find_next(grid, self.current_row)
            if next_position == [-1, -1]:
                break
            # Look for all connected land and mark them as checked
            self.depth_search_island(grid, next_position[0], next_position[1])
            # Add to count
            island_count += 1

        return island_count

    def depth_search_island(self, grid, x, y):
        """
        Recursively looks through the grid for connected land in depth-first search. Changes land to "checked" as it goes.

        Args:
            `grid`: A 2D array of `1` and `0`, with `1` representing land and
                `0` representing water.
            `x`: The x-position of the land to look at.
            `y`: The y-position of the land to look at.
        """

        # Mark this position as checked
        grid[y][x] = "-1"

        # Look left
        if x - 1 >= 0 and grid[y][x - 1] == "1":
            self.depth_search_island(grid, x - 1, y)
        # Look right
        if x + 1 < self.width and grid[y][x + 1] == "1":
            self.depth_search_island(grid, x + 1, y)
        # Look up
        if y - 1 >= 0 and grid[y - 1][x] == "1":
            self.depth_search_island(grid, x, y - 1)
        # Look down
        if y + 1 < self.height and grid[y + 1][x] == "1":
            self.depth_search_island(grid, x, y + 1)

        return

    def find_next(self, grid, start_row) -> list[int, int]:
        """
        Returns the 2D index of a next land to look at, if any.

        Args:
            `grid`: A 2D array of `1` and `0`, with `1` representing land and
                `0` representing water.
            `start_row`: The row to start looking at within `grid`.
        Returns:
            `position`: The x,y position of the next land to look at if there
                is one. Returns [-1,-1] if none found.
        """

        position = [-1, -1]
        for y in range(start_row, self.height):
            if "1" in grid[y]:
                position = [grid[y].index("1"), y]
                break
            self.current_row = y + 1
        return position
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and confidence in robustness.

We ran this for my solution and two other's solutions.

We checked for:

- A checkerboard setup of lands
- A ring of land, to been seen as one island.
- A single land in the list
- LeetCode's example cases
- All land & all water
- One row & one column
- Single item list. As land & water.

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

I used `tracemalloc` to look at peak memory block usage during the running of my solution `num_islands_1()` and two other people's solutions `num_islands_2()` and `num_islands_3()`.

This is tested with `test_1` of a checkerboard of islands.

My solution used the least memory of these three.

Memory blocks used:

- `num_islands_1()`: 600 blocks
- `num_islands_2()`: 704 blocks
- `num_islands_3()`: 624 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on the same test case.

My solution found the result in 52% the time of the slowest method.

- `num_islands_1()`: 5.230 x 10^-7 sec
- `num_islands_2()`: 9.294 x 10^-7 sec
- `num_islands_3()`: 10.02 x 10^-7 sec

## Reflections

My solution to this problem stores values in the `Solution` object. This object is only meant to survive for the time of calling of the function `num_islands_1()`. If called twice, there isn't any conflicts, but this could be seen as messy. We did this to reduce calls on the `grid` list length, and to allow the recursion to have access to these variables.

The other solutions define functions within their initial function, this feels equivalent to a private method in C++. I like that. My helper functions shouldn't be called on their own, not that they'd be of any help.

This LeetCode problem doesn't write for any handling of the initial `grid`, all the solutions here edit the `grid` as they go, which allows it to run faster for not having to copy the list. To run another function on this list would have a different outcome. To solve this, we'd do some copy method at the start.

## Solution Variations

### other_solution_2.py

`other_solution_2.py` uses Python's deque object as a stack of neighboring lands.

They first start looking through their `grid` with a double-nested loop, and when finding a first land, they look at it with `bfs(r,c)`. Then inside that, they use a while loop to continue looking for more connected lands while there are items in their deque. They edit these positions to be `"0"` water as they look at connected land.

```python
from collections import deque
class Solution:
    def num_islands_2(self, grid: list[list[str]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        def bfs(r, c):
            q = deque()
            q.append([r, c])
            while q:
                r, c = q.popleft()
                grid[r][c] = "0"
                for neiR, neiC in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if (
                        neiR in range(R)
                        and neiC in range(C)
                        and grid[neiR][neiC] == "1"
                    ):
                        q.append([neiR, neiC])
                        grid[neiR][neiC] = "0"
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    bfs(r, c)
                    ans += 1
        return ans
```

### other_solution_3.py

`other_solution_3.py` uses a similar logic to my solution.

I like that their solution is all within their initial method, but I see no reason not to split it up into two cooperative methods for encapsulation's sake.

By checking if a x,y position is valid within `dfs()` they end up calling all of these checks for each side of a currently looked at position. The `len(grid)`, which is costly on a large list, is called potentially eight times on each position being entered.

I avoid some amount of these checks by running my recursive search only on known valid pieces.

```python
class Solution:
    def num_islands_3(self, grid: list[list[str]]) -> int:
        def dfs(grid, r, c):
            if (
                r < 0
                or c < 0
                or r >= len(grid)
                or c >= len(grid[0])
                or grid[r][c] != "1"
            ):
                return
            grid[r][c] = "0"
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)
        num_of_islands = 0
        if not grid:
            return -1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    num_of_islands += 1
        return num_of_islands
```
