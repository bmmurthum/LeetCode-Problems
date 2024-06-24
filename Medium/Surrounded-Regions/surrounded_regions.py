""" Module to compute how many islands are represented in the list """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def solve_1(self, board: list[list[str]]) -> None:
        """
        Takes a 2D list of `"X"`s and `"O"`s and modifies the list to have surrounded Os be replaced with Xs.

        Args:
            `board`: The given 2D list being manipulated
        """

        def mark_connected(x, y, is_head, board):
            """
            Recursively looks at a region. Starting at a first-found `"O"`, we
            see if the region of `"O"`s should be surrounded, then we replace
            them with `"X"`. If the `"O"`s should stay, we mark them permanent
            as `"Q"` for later replacement back to `"O"`.

            Args:
                `x`: The current X-position of the spot we're looking at.
                `y`: The current Y-position of the spot we're looking at.
                `is_head`: If this position is where we started.
                `board`: The given 2D list being manipulated.
            Returns:
                `found_edge`: If this path has found an edge connection.
                `min_x`: The left-most position from head to any piece
                `max_x`: The right-most position ..
                `min_y`: The top-most position ..
                `max_y`: The bottom-most position ..
            """

            # If one of the paths found an edge
            found_edge_list = [False]
            # Lists of results from paths
            min_x_list = []
            max_x_list = []
            min_y_list = []
            max_y_list = []

            # If this is an edge
            if x == 0 or y == 0 or x + 1 == width or y + 1 == height:
                # return [True, x, x, y, y]
                found_edge_list.append(True)
                min_x_list.append(x)
                max_x_list.append(x)
                min_y_list.append(y)
                max_y_list.append(y)
            # If this is NOT an edge
            else:
                # Mark temporarily as a part of this region being looked at.
                board[y][x] = "T"

                # Add this position to be considered in max-min region.
                min_x_list.append(x)
                max_x_list.append(x)
                min_y_list.append(y)
                max_y_list.append(y)

                # Look left
                if board[y][x - 1] == "O":
                    a_found_edge, a_min_x, a_max_x, a_min_y, a_max_y = mark_connected(
                        x - 1, y, False, board
                    )
                    found_edge_list.append(a_found_edge)
                    min_x_list.append(a_min_x)
                    max_x_list.append(a_max_x)
                    min_y_list.append(a_min_y)
                    max_y_list.append(a_max_y)
                # Look right
                if board[y][x + 1] == "O":
                    b_found_edge, b_min_x, b_max_x, b_min_y, b_max_y = mark_connected(
                        x + 1, y, False, board
                    )
                    found_edge_list.append(b_found_edge)
                    min_x_list.append(b_min_x)
                    max_x_list.append(b_max_x)
                    min_y_list.append(b_min_y)
                    max_y_list.append(b_max_y)
                # Look up
                if board[y - 1][x] == "O":
                    c_found_edge, c_min_x, c_max_x, c_min_y, c_max_y = mark_connected(
                        x, y - 1, False, board
                    )
                    found_edge_list.append(c_found_edge)
                    min_x_list.append(c_min_x)
                    max_x_list.append(c_max_x)
                    min_y_list.append(c_min_y)
                    max_y_list.append(c_max_y)
                # Look down
                if board[y + 1][x] == "O":
                    d_found_edge, d_min_x, d_max_x, d_min_y, d_max_y = mark_connected(
                        x, y + 1, False, board
                    )
                    found_edge_list.append(d_found_edge)
                    min_x_list.append(d_min_x)
                    max_x_list.append(d_max_x)
                    min_y_list.append(d_min_y)
                    max_y_list.append(d_max_y)

            # Find min-max position values from paths that were searched.
            min_x = min(min_x_list)
            max_x = max(max_x_list)
            min_y = min(min_y_list)
            max_y = max(max_y_list)

            # Did one of the paths find an edge?
            found_edge = True in found_edge_list

            # If not head of recursion, return up.
            if not is_head:
                return [found_edge, min_x, max_x, min_y, max_y]

            # After looking through and found edge,
            # mark these to be confirmed Qs or Xs within range
            if is_head and found_edge:
                for x in range(min_x, max_x + 1):
                    for y in range(min_y, max_y + 1):
                        if board[y][x] == "T":
                            board[y][x] = "Q"
            if is_head and not found_edge:
                for x in range(min_x, max_x + 1):
                    for y in range(min_y, max_y + 1):
                        if board[y][x] == "T":
                            board[y][x] = "X"

        # Note the board size
        width = len(board[0])
        height = len(board)

        # No possibility of changes. Return with no changes.
        if width <= 2 or height <= 2:
            return

        # Look through 2D list for a region to look at.
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                if board[y][x] == "O":
                    mark_connected(x, y, True, board)

        # Replace any marked to stay, "Q", back to "O".
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                if board[y][x] == "Q":
                    board[y][x] = "O"
