""" Module to apply next step to Conway's Game of Life. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


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
