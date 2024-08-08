"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def spiral_matrix_iii(
        self, rows: int, cols: int, r_start: int, c_start: int
    ) -> list[list[int]]:
        """
        You start at position `r_start` `c_start` and move in a spiral pattern.
        This method builds a list of the positions you'll meet on the grid in
        the order that you visit them.

        Args:
            `rows`: The number of rows in the list.
            `cols`: The number of columns in the list.
            `r_start`: The row you start on.
            `c_start`: The column you start on.
        Returns:
            `output_list`: The list of positions you visit.
        """

        # Keep a count integer.
        # Keep the ordered list of positions visited.
        # Keep a hash-searchable "has been here?"
        # We're looking for when `count` meets `goal`.
        count = 1
        visited = []
        visited_hash = set()
        goal = rows * cols

        # Keep position markers.
        furthest_right = c_start
        furthest_left = c_start
        furthest_up = r_start
        furthest_down = r_start
        current_row = r_start
        current_col = c_start

        # Add first item
        visited.append([current_row, current_col])
        visited_hash.add((current_row, current_col))

        # Loop the spiral
        while count < goal:

            # Move right
            # - If the item to the right has been visited, we're at a top, move
            #   to the right as far as possible.
            # - If not, step to the right until past the furthest.
            if (current_row, current_col + 1) in visited_hash:
                if furthest_right == cols - 1:
                    current_col = furthest_right
                else:
                    current_col = furthest_right + 1
                    visited.append([current_row, current_col])
                    visited_hash.add((current_row, current_col))
                    count += 1
                    furthest_right = current_col
            else:
                while current_col <= furthest_right and current_col < cols - 1:
                    current_col += 1
                    visited.append([current_row, current_col])
                    visited_hash.add((current_row, current_col))
                    count += 1
                if current_col > furthest_right:
                    furthest_right = current_col

            # Move down
            if (current_row + 1, current_col) in visited_hash:
                if furthest_down == rows - 1:
                    current_row = furthest_down
                else:
                    current_row = furthest_down + 1
                    visited.append([current_row, current_col])
                    visited_hash.add((current_row, current_col))
                    count += 1
                    furthest_down = current_row
            else:
                while current_row <= furthest_down and current_row < rows - 1:
                    current_row += 1
                    visited.append([current_row, current_col])
                    visited_hash.add((current_row, current_col))
                    count += 1
                if current_row > furthest_down:
                    furthest_down = current_row

            # Move left
            if (current_row, current_col - 1) in visited_hash:
                if furthest_left == 0:
                    current_col = furthest_left
                else:
                    current_col = furthest_left - 1
                    visited.append([current_row, current_col])
                    visited_hash.add((current_row, current_col))
                    count += 1
                    furthest_left = current_col
            else:
                while current_col >= furthest_left and current_col > 0:
                    current_col -= 1
                    visited.append([current_row, current_col])
                    visited_hash.add((current_row, current_col))
                    count += 1
                if current_col < furthest_left:
                    furthest_left = current_col

            # Move up
            if (current_row - 1, current_col) in visited_hash:
                if furthest_up == 0:
                    current_row = furthest_up
                else:
                    current_row = furthest_up - 1
                    visited.append([current_row, current_col])
                    visited_hash.add((current_row, current_col))
                    count += 1
                    furthest_up = current_row
            else:
                while current_row >= furthest_up and current_row > 0:
                    current_row -= 1
                    visited.append([current_row, current_col])
                    visited_hash.add((current_row, current_col))
                    count += 1
                if current_row < furthest_up:
                    furthest_up = current_row

        # Return the requested list of positions.
        return visited
