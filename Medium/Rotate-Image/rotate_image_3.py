""" Module to rotate a matrix 90 degrees. """


class Solution:
    """Problem given by LeetCode."""

    def rotate_3(self, matrix: list[list[int]]) -> None:
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
