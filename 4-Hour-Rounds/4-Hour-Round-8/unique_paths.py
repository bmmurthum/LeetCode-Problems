"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def unique_paths(self, m: int, n: int) -> int:
        """
        Looking at a grid sized `m` x `n`, with a robot that can move right and
        downward, how many different paths can the robot take to get to the
        bottom right?

        Args:
            `n`: The width of the grid.
            `m`: The height of the grid.
        Returns:
            `output`: The number of different paths that can be taken.
        """

        # Edge-case: The grid is one-high or one-wide.
        if n == 1 or m == 1:
            return 1
        # Edge-case: The grid is easy to solve without iteration.
        if n == 2:
            return m
        if m == 2:
            return n

        # Initialize a grid with all zeroes except for 1s in top row and left
        # column.
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(grid[0])):
            grid[0][i] = 1
        for j in range(len(grid)):
            grid[j][0] = 1

        # Starting at [1,1] generate the board with calculations based on the
        # item above and to its left. Each value will represent how many paths
        # can be take to reach that point.
        for x in range(1, len(grid[0])):
            for y in range(1, len(grid)):
                grid[y][x] = grid[y - 1][x] + grid[y][x - 1]

        # The bottom right corner's value represents the number of paths to
        # reach this point.
        output = grid[len(grid) - 1][len(grid[0]) - 1]
        return output
