""" Module to compute how many islands are represented in the list """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


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
