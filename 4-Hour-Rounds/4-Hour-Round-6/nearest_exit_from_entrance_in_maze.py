"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def nearest_exit(self, maze: list[list[str]], entrance: list[int]) -> int:
        """
        Finds the shortest distance to an "exit" of a maze from the given start
        position. An exit is a position at the edge of the maze which is not the starting position.

        Args:
            `maze`: A 2-d list representing the maze.
            `entrance`: An initial coordinate that the person is positioned at.
        Returns:
            `steps`: A number of steps to exit the maze.
        """

        def is_exit(maze, entrance, y, x) -> bool:
            """Returns True if this position is an exit."""
            if y == entrance[0] and x == entrance[1]:
                return False
            if y == 0 or x == 0:
                return True
            if x == len(maze[0]) - 1 or y == len(maze) - 1:
                return True
            return False

        def next_possible_positions(maze, y, x) -> list:
            """Returns a list of next positions."""

            # Up, Down, Left, Right
            # Consider's walls, previously visited, edges

            output = []
            if y > 0 and maze[y - 1][x] == ".":
                output.append([y - 1, x])
            if y < len(maze) - 1 and maze[y + 1][x] == ".":
                output.append([y + 1, x])
            if x > 0 and maze[y][x - 1] == ".":
                output.append([y, x - 1])
            if x < len(maze[0]) - 1 and maze[y][x + 1] == ".":
                output.append([y, x + 1])
            return output

        # Do a BFS on the maze, keeping track of steps as we go.
        # If all branches reach ends without exit, we return a failure case.
        current_positions = [entrance]
        maze[entrance[0]][entrance[1]] = 0
        while len(current_positions) > 0:
            position = current_positions[0]
            current_positions.pop(0)
            if is_exit(maze, entrance, position[0], position[1]):
                return maze[position[0]][position[1]]
            temp = next_possible_positions(maze, position[0], position[1])
            for new in temp:
                current_positions.append(new)
                maze[new[0]][new[1]] = maze[position[0]][position[1]] + 1
        return -1
