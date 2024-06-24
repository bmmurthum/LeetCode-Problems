from collections import deque


class Solution:

    def num_islands_2(self, grid: list[list[str]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0

        def bfs(r, c):
            q = deque()
            q.append([r, c])
            while q:
                r, c = q.popleft()
                grid[r][c] = "0"
                for neiR, neiC in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if (
                        neiR in range(R)
                        and neiC in range(C)
                        and grid[neiR][neiC] == "1"
                    ):
                        q.append([neiR, neiC])
                        grid[neiR][neiC] = "0"

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    bfs(r, c)
                    ans += 1

        return ans
