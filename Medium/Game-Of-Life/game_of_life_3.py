class Solution:

    def game_of_life_3(self, board: list[list[int]]) -> None:
        N = len(board)
        M = len(board[0])

        copy = [[0 for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                copy[i][j] = board[i][j]

        for r in range(N):
            for c in range(M):
                count = 0
                for i, j in [
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0),
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1),
                ]:  # 8 neighbours to check
                    if (
                        r + i >= 0
                        and c + j >= 0
                        and r + i < N
                        and c + j < M
                        and copy[r + i][c + j] == 1
                    ):  # valid neighbour
                        count += 1
                if count < 2:  # die
                    board[r][c] = 0
                elif count > 3:  # die
                    board[r][c] = 0
                elif count == 3:  # live
                    board[r][c] = 1
