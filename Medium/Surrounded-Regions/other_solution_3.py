class Solution:
    def solve_3(self, board: list[list[str]]) -> None:
        for i in range(len(board)):
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            if board[i][len(board[0]) - 1] == "O":
                self.dfs(board, i, len(board[0]) - 1)
        for j in range(len(board[0])):
            if board[0][j] == "O":
                self.dfs(board, 0, j)
            if board[len(board) - 1][j] == "O":
                self.dfs(board, len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"

    def dfs(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == "O":
            board[i][j] = "#"
            self.dfs(board, i + 1, j)
            self.dfs(board, i - 1, j)
            self.dfs(board, i, j + 1)
            self.dfs(board, i, j - 1)
