class Solution:
    def set_zeroes_3(self, matrix: list[list[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        zeroCol = [False] * COLS
        zeroRow = [False] * (ROWS)
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeroCol[c] = True
                    zeroRow[r] = True
        for r in range(ROWS):
            if zeroRow[r]:
                for c in range(COLS):
                    matrix[r][c] = 0
        for c in range(COLS):
            if zeroCol[c]:
                for r in range(ROWS):
                    matrix[r][c] = 0
        return
