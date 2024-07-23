# Game of Life

**Description:**

According to [Wikipedia's article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: live (represented by a `1`) or dead (represented by a `0`). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the `m x n` grid `board`, return the next state.

**Constraints:**

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 25`
- `board[i][j] is 0 or 1`

**Follow up:**

- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

**Examples:**

```python
# 0 1 0     0 0 0
# 0 0 1  >  1 0 1
# 1 1 1     0 1 1
# 0 0 0     0 1 0
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: result = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# 1 1     1 1
# 1 0  >  1 1
Input: board = [[1,1],[1,0]]
Output: result = [[1,1],[1,1]]
```

## Overview

My solution introduces a helping internal method `neighbor_count()` which will count the live-neighbors at a given x-y position and take into consideration whether it's at a border.

Trying to solve this with little memory usage, we're doing this process in-place.

1. Iterate through the 2D list `board` looking at each position's neighbor count and decide if it would be changed in the next position.
    - Values that were `0` and will change to `1` are marked `#`.
    - Values that were `1` and will change to `0` are marked `*`.
    - With these we can keep memory of last position and what it will be. This allows us to check both `1` and `*` as live neighbors.
2. After setting all the new values, we change these temp values of `#` and `*` to their respective `1` and `0`.

```python
class Solution:
    """Problem given by LeetCode."""

    def game_of_life(self, board: list[list[int]]) -> None:
        """
        Modifies a given 2D list in-place to apply the next step to Conway's
        Game of Life.

        Args:
            `board`: The given 2D list to be modified.
        Returns:
            `None`
        """

        def neighbor_count(x: int, y: int, board: list[list[int]]) -> int:
            """Returns the number of living neighbors."""

            width = len(board[0])
            height = len(board)

            # Be aware of edges of matrix
            left, right, top, bottom = True, True, True, True
            if x - 1 < 0:
                left = False
            if x + 1 >= width:
                right = False
            if y - 1 < 0:
                top = False
            if y + 1 >= height:
                bottom = False

            # Count neighbors
            count = 0
            if top:
                if board[y - 1][x] == 1 or board[y - 1][x] == "*":
                    count += 1
                if left:
                    if board[y - 1][x - 1] == 1 or board[y - 1][x - 1] == "*":
                        count += 1
                if right:
                    if board[y - 1][x + 1] == 1 or board[y - 1][x + 1] == "*":
                        count += 1
            if left:
                if board[y][x - 1] == 1 or board[y][x - 1] == "*":
                    count += 1
            if right:
                if board[y][x + 1] == 1 or board[y][x + 1] == "*":
                    count += 1
            if bottom:
                if board[y + 1][x] == 1 or board[y + 1][x] == "*":
                    count += 1
                if left:
                    if board[y + 1][x - 1] == 1 or board[y + 1][x - 1] == "*":
                        count += 1
                if right:
                    if board[y + 1][x + 1] == 1 or board[y + 1][x + 1] == "*":
                        count += 1
            return count

        # 0 -> "#" Will change to 1
        # 1 -> "*" Will change to 0
        width = len(board[0])
        height = len(board)

        # Set the board for the next iteration, with memory of last.
        for x in range(width):
            for y in range(height):
                num = neighbor_count(x, y, board)
                if board[y][x] == 0 and num == 3:
                    board[y][x] = "#"
                    continue
                if board[y][x] == 1:
                    if not (num == 2 or num == 3):
                        board[y][x] = "*"
                        continue
        # Clear midway-positions
        for x in range(width):
            for y in range(height):
                if board[y][x] == "#":
                    board[y][x] = 1
                elif board[y][x] == "*":
                    board[y][x] = 0
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and general confidence.

We ran this for my solution `game_of_life` and two other people's solutions.

We checked for:

- LeetCode's two example cases.
- 4x3 case of all `1`.
- Mixed case of 3x3.
- 3x3 case of all `0`.
- 1x1 case of `1` and `0`.
- Two different 1x3 cases.
- A 10x10 case generated from an [external site](https://conwaylife.com/).

### Code Coverage

We received 100% code coverage on my methods from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run -m unittest
> coverage report
Name                Stmts   Miss  Cover
---------------------------------------
game_of_life.py        58      0   100%
game_of_life_2.py      24      0   100%
game_of_life_3.py      20      0   100%
test_unittests.py     101      0   100%
testcases.py           41      0   100%
---------------------------------------
TOTAL                 244      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution `game_of_life()` against the others' solutions.

**Test 10:** 10x10 case.

- `game_of_life()`: 744 blocks
- `game_of_life_2()`: 2120 blocks
- `game_of_life_3()`: 1880 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on a test cases.

Note, that the recorded time includes a `deepcopy()` of the given test.

**Test 10:** 10x10 case.

- `game_of_life()`: 9.285 x 10^-5 sec
- `game_of_life_2()`: 13.450 x 10^-5 sec
- `game_of_life_3()`: 10.685 x 10^-5 sec

## Reflections

I'm happy to see that this in-place solution out-performs other solutions that include an internal copying of the 2D list.

If I were to spend more time with this, I may rewrite the internal `neighbor_count()` to be simpler, or try for less calls. I could take a note from these other two solutions.

## Solution Variations

### game_of_life_2.py

Their use of a matching size list `ans` costs double memory and costs the time of both calling for that memory and assigning each value. I'd look to lose this, unless the cost of memory ended up speeding up the process.

I like their logic of `inBound()`, very clean.

Their chained `elif` could be boiled down in logic to avoid so many calls.

The `board[:] = ans` is time-consuming and could be avoided with in-place logic. They also do not have to return `board` per the constraints.

```python
class Solution:
    def game_of_life_2(self, board: list[list[int]]) -> None:
        rowLen = len(board[0])
        colLen = len(board)
        ans = [[-1 for x in range(rowLen)] for y in range(colLen)]

        def inBound(i, j):
            return (0 <= i < colLen) and (0 <= j < rowLen)
        for i in range(colLen):
            for j in range(rowLen):
                count = 0
                for ii, jj in [
                    (i, j + 1),
                    (i, j - 1),
                    (i - 1, j),
                    (i + 1, j),
                    (i - 1, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j + 1),
                    (i - 1, j - 1),
                ]:
                    if inBound(ii, jj):
                        count += board[ii][jj]
                if count < 2:
                    ans[i][j] = 0
                elif board[i][j] == 1 and (count == 2 or count == 3):
                    ans[i][j] = 1
                elif board[i][j] == 1 and count > 3:
                    ans[i][j] = 0
                elif board[i][j] == 0 and count == 3:
                    ans[i][j] = 1
                else:
                    ans[i][j] = board[i][j]
        board[:] = ans
        return board
```

### game_of_life_3.py

This person does similar process to the last. They pull the logic of checking valid neighbors out from a function.

They use a copy of the initial list `copy` to hold the old values, while changing values in `board`.

I would suggest that their variables be named more verbose. `N` to `WIDTH`, `r` to `rows`, etc.

```python
class Solution:
    def game_of_life_3(self, board: list[list[int]]) -> None:
        N = len(board)
        M = len(board[0])
        copy = [[0 for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                copy[i][j] = board[i][j]
        for r in range(N):
            for c in range(M):
                count = 0
                for i, j in [
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0),
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1),
                ]:  # 8 neighbours to check
                    if (
                        r + i >= 0
                        and c + j >= 0
                        and r + i < N
                        and c + j < M
                        and copy[r + i][c + j] == 1
                    ):  # valid neighbour
                        count += 1
                if count < 2:  # die
                    board[r][c] = 0
                elif count > 3:  # die
                    board[r][c] = 0
                elif count == 3:  # live
                    board[r][c] = 1
```
