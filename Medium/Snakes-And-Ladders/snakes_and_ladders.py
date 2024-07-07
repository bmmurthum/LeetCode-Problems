""" Module to return the minimum number of steps in a snakes and ladder board game. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def __init__(self) -> None:
        self.rows = None
        self.cols = None
        self.board = None

    def snakes_and_ladders(self, board: list[list[int]]) -> int:
        """
        Returns the minimum number of moves to complete the board. If impossible, returns -1.

        https://en.wikipedia.org/wiki/Boustrophedon

        List is organized in a Boustrophedon styled path, starting at bottom left.

        Args:
            `board`: A 2D list representing a snakes and ladders board game.
                Where each value represents the position that landing on this
                spot would take the player to.
        Returns:
            `h_index`: The value.
        """
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        least_steps = self.find_least(1, 0, [])
        return least_steps

    def get_row_column(self, position: int) -> list[int, int]:
        """
        Returns the specific row-col coordinates of an actual board position.

        Args:
            `position`: The number written on the board.
        Returns:
            `new_y`: The y-position in the `board` list.
            `new_x`: The x-position in the `board` list.
        """
        temp_x = (position - 1) % self.cols
        new_x = None
        temp_y = (position - 1) // self.cols
        if temp_y == 0 or temp_y % 2 == 0:
            new_x = temp_x
        else:
            new_x = self.cols - 1 - temp_x
        new_y = self.rows - 1 - temp_y
        return [new_y, new_x]

    def get_new_position(self, position: int) -> int:
        """
        Return the position that this position takes you to. If not a snake/
        ladder, returns the initial given position.

        Args:
            `position`: The position to look at.
        Returns:
            `new_position`: The position the given position takes you to, or
                itself.
        """
        y, x = self.get_row_column(position)
        new_position = self.board[y][x]
        if new_position == -1:
            return position
        else:
            return new_position

    def find_least(
        self,
        position: int,
        current_step: int,
        visited_list,
    ) -> int:
        """
        Recursively looks to find a least-steps path to the last position.

        Args:
            `position`: Position to start search on.
            `current_step`: The current count of steps. `0` if top.
            `board`: The board
            `visited_list`: The list of visited positions.
        Returns:
            `min_steps`: The number of steps to get to the final position.
                In some cases, this is `-1` to suggest no path can reach.
        """
        # Add a visit note, if we started at this position.
        new_visited_list = visited_list.copy()
        # new_visited_list = visited_list
        new_visited_list.append(position)
        # Step count
        new_step = current_step + 1

        # On reaching the end, return number of steps.
        if position == self.rows**2:
            return current_step
        # If final position is within 6, return now, without searching.
        # Allows us to avoid writing catches for overstepping the final.
        elif position + 6 >= self.rows**2:
            return current_step + 1

        # Build a list of positions to recursively move to.
        min_steps = 500
        for i in range(6, 0, -1):
            check = position + i
            new_position = self.get_new_position(check)
            # If position is beginning of snake/ladder add it to list
            if new_position != check and new_position not in new_visited_list:
                temp = self.find_least(new_position, new_step, new_visited_list)
                if temp != -1 and temp < min_steps:
                    min_steps = temp
        # Find farthest position without traveling.
        max_without_travel = -2
        for i in range(6, 0, -1):
            check = position + i
            new_position = self.get_new_position(check)
            if new_position == check:
                max_without_travel = check
                break
        # If couldn't find anything to walk further.
        if max_without_travel != -2 and max_without_travel not in new_visited_list:
            temp = self.find_least(max_without_travel, new_step, new_visited_list)
            if temp != -1 and temp < min_steps:
                min_steps = temp
        # If never found a spot to go to.
        if min_steps == 500:
            return -1
        return min_steps
