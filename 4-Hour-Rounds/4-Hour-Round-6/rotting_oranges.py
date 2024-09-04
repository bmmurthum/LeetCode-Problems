"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def oranges_rotting(self, grid: list[list[int]]) -> int:
        """
        Given a 2-d list that represent oranges, "fresh" and "rotting",
        consider the amount of "time," or steps, until all are rotted. A fresh
        orange will turn to rotting if adjacent to a rotting one in the last
        step.

        Return -1 if there is no amount of time that will rot all oranges.

        Args:
            `grid`: A 2-d list representing the oranges.
        Returns:
            `steps`: A number of steps to all rotted oranges.
        """

        def touching_another_orange(grid, y, x) -> bool:
            """Tells us if an orange is touching another."""
            if x != 0 and grid[y][x - 1] != 0:
                return True
            if y != 0 and grid[y - 1][x] != 0:
                return True
            if x < len(grid[0]) - 1 and grid[y][x + 1] != 0:
                return True
            if y < len(grid) - 1 and grid[y + 1][x] != 0:
                return True
            return False

        def next_oranges(grid, y, x) -> list:
            """Return a list of touching oranges to spoil."""
            output = []
            if x != 0 and grid[y][x - 1] == 1:
                output.append([y, x - 1])
            if y != 0 and grid[y - 1][x] == 1:
                output.append([y - 1, x])
            if x < len(grid[0]) - 1 and grid[y][x + 1] == 1:
                output.append([y, x + 1])
            if y < len(grid) - 1 and grid[y + 1][x] == 1:
                output.append([y + 1, x])
            return output

        # Build initial conditions, check for edge-cases.
        # - An orange not touching any others, will never spoil.
        # - If no fresh oranges, immediately return 0
        # - If no rotten, they will never spoil.
        # - If no oranges, there's nothing to spoil.
        rotten_oranges = []
        initial_fresh = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    rotten_oranges.append([y, x])
                if grid[y][x] == 1:
                    initial_fresh += 1
                    if touching_another_orange(grid, y, x) is False:
                        return -1
        if initial_fresh == 0:
            return 0
        if len(rotten_oranges) == 0 and initial_fresh != 0:
            return -1

        # Add the initial rotten oranges to a queue.
        # Count steps in breadth search downward from -1
        # Keep count of fresh oranges to check on when no more can be rotted.
        queue = rotten_oranges.copy()
        last_step = 0
        for item in queue:
            grid[item[0]][item[1]] = -1
        while len(queue) != 0:
            current = queue[0]
            queue.pop(0)
            temp = next_oranges(grid, current[0], current[1])
            for item in temp:
                grid[item[0]][item[1]] = grid[current[0]][current[1]] - 1
                last_step = grid[current[0]][current[1]] - 1
                initial_fresh -= 1
                queue.append(item)
        if initial_fresh > 0:
            return -1
        return -1 * (last_step + 1)
