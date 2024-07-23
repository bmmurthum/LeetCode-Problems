""" Module to change columns and rows of a matrix to zeroes. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def set_zeroes(self, matrix: list[list[int]]) -> None:
        """
        Modifies a given matrix in-place to have values in a row or col
        containing a zero all be now set to zero. Modifies in-place.

        Args:
            `matrix`: The given 2D list to be modified.
        Returns:
            `None`
        """

        width = len(matrix[0])
        height = len(matrix)

        # Handle marking rows and cols
        for x in range(width):
            for y in range(height):
                if matrix[y][x] == 0:
                    for x_i in range(width):
                        if matrix[y][x_i] != 0:
                            matrix[y][x_i] = "#"
                    for y_i in range(height):
                        if matrix[y_i][x] != 0:
                            matrix[y_i][x] = "#"
        # Replace marks with zeroes
        for x in range(width):
            for y in range(height):
                if matrix[y][x] == "#":
                    matrix[y][x] = 0

    def set_zeroes_b(self, matrix: list[list[int]]) -> None:
        """
        Modifies a given matrix in-place to have values in a row or col
        containing a zero all be now set to zero. Modifies in-place.

        Args:
            `matrix`: The given 2D list to be modified.
        Returns:
            `None`
        """

        width = len(matrix[0])
        height = len(matrix)

        # Handle marking which rows and cols to change later
        for x in range(width):
            for y in range(height):
                if matrix[y][x] == 0:
                    if matrix[0][x] != 0:
                        matrix[0][x] = "#"
                    if matrix[y][0] != 0:
                        matrix[y][0] = "#"
        # Handle cols
        for x in range(1, width):
            if matrix[0][x] == 0:
                for i in range(width):
                    if matrix[0][i] != 0 and matrix[0][i] != "#":
                        matrix[0][i] = "*"
                for i in range(height):
                    matrix[i][x] = 0
            if matrix[0][x] == "#":
                for i in range(height):
                    matrix[i][x] = 0
        # Handle rows
        for y in range(1, height):
            if matrix[y][0] == 0:
                for i in range(height):
                    if matrix[i][0] != 0 and matrix[i][0] != "#":
                        matrix[i][0] = "*"
                for i in range(width):
                    matrix[y][i] = 0
            if matrix[y][0] == "#":
                for i in range(width):
                    matrix[y][i] = 0
        # Clean top left corner
        if matrix[0][0] == "#" or matrix[0][0] == "*":
            matrix[0][0] = 0
        elif matrix[0][0] == 0:
            for x in range(width):
                matrix[0][x] = 0
            for y in range(height):
                matrix[y][0] = 0
        # Clean top row
        for x in range(width):
            if matrix[0][x] == "*":
                matrix[0][x] = 0
        # Clean left column
        for y in range(height):
            if matrix[y][0] == "*":
                matrix[y][0] = 0
