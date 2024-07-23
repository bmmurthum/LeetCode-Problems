""" Module to rotate a matrix 90 degrees. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Modifies a given matrix in-place to have all the values be 'rotated' 90
        degrees in their positions.

        Args:
            `matrix`: The given 2D list to be modified.
        Returns:
            `None`
        """

        width = len(matrix)
        if width == 1:
            return

        # Create a list of all the positions in the top-left quadrant.
        is_odd_width = None
        if width % 2 == 1:
            is_odd_width = True
        else:
            is_odd_width = False
        change_list = []
        if is_odd_width:
            for x in range(0, (width // 2)):
                for y in range(0, (width // 2) + 1):
                    change_list.append([x, y])
        else:
            for x in range(0, width // 2):
                for y in range(0, width // 2):
                    change_list.append([x, y])

        # Change values in place.
        for _, item in enumerate(change_list):
            # Top left to top right
            value = matrix[item[1]][item[0]]
            new_x = width - 1 - item[1]
            new_y = item[0]
            temp = matrix[new_y][new_x]
            matrix[new_y][new_x] = value
            value = temp
            # Top right to bottom right
            new_x = width - 1 - item[0]
            new_y = width - 1 - item[1]
            temp = matrix[new_y][new_x]
            matrix[new_y][new_x] = value
            value = temp
            # Bottom right to bottom left
            new_x = item[1]
            new_y = width - 1 - item[0]
            temp = matrix[new_y][new_x]
            matrix[new_y][new_x] = value
            value = temp
            # Bottom left to top left
            matrix[item[1]][item[0]] = value

    def rotate_b(self, matrix: list[list[int]]) -> None:
        """
        Modifies a given matrix in-place to have all the values be 'rotated' 90
        degrees in their positions.

        Args:
            `matrix`: The given 2D list to be modified.
        Returns:
            `None`
        """

        # Without the remove list. Uses less memory, faster.

        width = len(matrix)
        if width == 1:
            return
        if width % 2 == 1:
            for x in range(0, (width // 2)):
                for y in range(0, (width // 2) + 1):
                    # Top left to top right
                    value = matrix[x][width - 1 - y]
                    matrix[x][width - 1 - y] = matrix[y][x]
                    # Top right to bottom right
                    a = matrix[width - 1 - y][width - 1 - x]
                    matrix[width - 1 - y][width - 1 - x] = value
                    # Bottom right to bottom left
                    b = matrix[width - 1 - x][y]
                    matrix[width - 1 - x][y] = a
                    # Bottom left to top left
                    matrix[y][x] = b
        else:
            for x in range(0, width // 2):
                for y in range(0, width // 2):
                    # Top left to top right
                    value = matrix[x][width - 1 - y]
                    matrix[x][width - 1 - y] = matrix[y][x]
                    # Top right to bottom right
                    a = matrix[width - 1 - y][width - 1 - x]
                    matrix[width - 1 - y][width - 1 - x] = value
                    # Bottom right to bottom left
                    b = matrix[width - 1 - x][y]
                    matrix[width - 1 - x][y] = a
                    # Bottom left to top left
                    matrix[y][x] = b

    def rotate_c(self, matrix: list[list[int]]) -> None:
        """
        Modifies a given matrix in-place to have all the values be 'rotated' 90
        degrees in their positions.

        Args:
            `matrix`: The given 2D list to be modified.
        Returns:
            `None`
        """

        # Condensed, with less helper variables to save on memory calls.

        width = len(matrix)
        if width == 1:
            return
        y_range = width // 2
        if width % 2 == 1:
            y_range = (width // 2) + 1
        for x in range(width // 2):
            for y in range(y_range):
                value = matrix[y][x]
                matrix[y][x] = matrix[width - 1 - x][y]
                matrix[width - 1 - x][y] = matrix[width - 1 - y][width - 1 - x]
                matrix[width - 1 - y][width - 1 - x] = matrix[x][width - 1 - y]
                matrix[x][width - 1 - y] = value
