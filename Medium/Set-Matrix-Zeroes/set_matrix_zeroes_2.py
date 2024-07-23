class Solution:
    def set_zeroes_2(self, matrix: list[list[int]]) -> None:
        lr = len(matrix)
        lc = len(matrix[0])

        row = [0] * lr
        col = [0] * lc

        for i in range(lr):
            for j in range(lc):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(lr):
            for j in range(lc):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0
        return matrix
