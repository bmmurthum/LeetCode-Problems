class Solution:

    def num_islands_3(self, grid: list[list[str]]) -> int:
        def dfs(grid, r, c):
            if (
                r < 0
                or c < 0
                or r >= len(grid)
                or c >= len(grid[0])
                or grid[r][c] != "1"
            ):
                return
            grid[r][c] = "0"
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)

        num_of_islands = 0
        if not grid:
            return -1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    num_of_islands += 1
        return num_of_islands
