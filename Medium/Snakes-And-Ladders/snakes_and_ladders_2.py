""" Module to return the minimum number of steps in a snakes and ladder board game. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201

from collections import deque


class Solution:
    """Problem given by LeetCode."""

    def snakes_and_ladders_2(self, board: list[list[int]]) -> int:
        """
        Returns the minimum number of moves to complete the board. If impossible, returns -1.

        https://en.wikipedia.org/wiki/Boustrophedon

        List is organized in a Boustrophedon styled path, starting at bottom left.

        Args:
            `board`: A 2D list representing a snakes and ladders board game.
                Where each value represents the position that landing on this
                spot would take the player to.
        Returns:
            `least_steps`: The minimum number of steps to complete the game.
        """
        self.last_index = (len(board) ** 2) - 1
        rows = len(board[0])
        new_board = self.reduce_board(board, rows)
        least_steps = self.find_least(new_board)
        return least_steps

    def reduce_board(self, board, rows) -> list:
        """
        Outputs an equivalent board that is 1 dimensional. Each value points to
        a more valid index, instead of given "position on playing board."

        Args:
            `board`: Initial 2D board.
            `rows`: Rows/Cols of the initial board.
        Returns:
            `new_board`: A simpler board.
        """
        new_board = []
        for i in range(rows - 1, -1, -1):
            if (rows - i) % 2 == 1:
                for item in board[i]:
                    new_board.append(item)
            else:
                temp = board[i]
                temp.reverse()
                for item in temp:
                    new_board.append(item)
        # Align values to list indexes
        for i, item in enumerate(new_board):
            if item > 0:
                new_board[i] = item - 1
        return new_board

    def find_next_steps(self, board, position) -> list:
        """
        Returns a list of potential next steps to choose. Finds interesting
        moves:
          - Furthest without snake/ladder
          - Any entrances to snakes/ladders

        Args:
            `board`: The 1-D board.
            `position`: Our current position index.
        Returns:
            `return_list`: A list of new indexes to move to.
        """
        return_list = []
        # Any snakes and ladders
        for i in range(6, 0, -1):
            new_position = board[position + i]
            if new_position > 0:
                return_list.append(position + i)
        # Farthest position without traveling
        for i in range(6, 0, -1):
            if board[position + i] == -1:
                return_list.append(position + i)
                break
        return return_list

    def find_least(
        self,
        board: list,
    ) -> int:
        """
        Breadth-first search to look for least-steps-path to the last position.

        Args:
            `board`: The 1-D board
        Returns:
            `step_count`: The number of steps to get to the final position.
                In some cases, this is `-1` to suggest no path can reach.
        """
        # Add a visit note, if we started at this position.
        visited = [False] * (self.last_index + 1)
        visited[0] = True

        queue = deque()
        temp_queue = deque()
        queue.append(0)

        step_count = 0
        while queue:
            current = queue.popleft()
            # Stop when done.
            if current + 6 >= self.last_index:
                return step_count + 1
            # Consider which positions to look at next.
            next_steps = self.find_next_steps(board, current)
            for step in next_steps:
                if not visited[step]:
                    visited[step] = True
                    if board[step] == -1:
                        temp_queue.append(step)
                    elif board[step] == self.last_index:
                        return step_count + 1
                    else:
                        temp_queue.append(board[step])
            # Set up next steps in queue
            if len(queue) == 0:
                queue = temp_queue.copy()
                temp_queue.clear()
                step_count += 1

        # Return -1 if the loop never found the ending.
        return -1
