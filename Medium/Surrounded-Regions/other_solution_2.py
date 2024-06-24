class Solution:
    __X = "X"
    __O = "O"

    def __init__(self):
        self.grid, self.ROWS, self.COLS, self.visited = None, None, None, None
        self.banned = set()

    def in_range(self, i, j):
        return 0 <= i < self.ROWS and 0 <= j < self.COLS

    @staticmethod
    def get_neighbors(i, j):
        return ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))

    def dfs(self, i, j):
        if (
            not self.in_range(i, j)
            or self.visited[i][j]
            or not self.grid[i][j] == self.__O
        ):
            return

        self.visited[i][j] = True
        self.banned.add((i, j))

        for x, y in self.get_neighbors(i, j):
            self.dfs(x, y)

    def solve_2(self, board: list[list[str]]) -> None:
        grid = board
        self.grid, self.ROWS, self.COLS = grid, len(grid), len(grid[0])
        self.visited = [[False] * self.COLS for _ in range(self.ROWS)]

        corners = []

        for i in range(1, self.ROWS - 1):
            if self.grid[i][0] == self.__O:
                corners.append((i, 0))
            if 0 < self.COLS - 1 and self.grid[i][self.COLS - 1] == self.__O:
                corners.append((i, self.COLS - 1))

        for j in range(self.COLS):
            if self.grid[0][j] == self.__O:
                corners.append((0, j))
            if 0 < self.ROWS - 1 and self.grid[self.ROWS - 1][j] == self.__O:
                corners.append((self.ROWS - 1, j))

        for i, j in corners:
            self.dfs(i, j)

        self.banned = self.banned.difference(set(corners))

        for i in range(1, self.ROWS - 1):
            for j in range(1, self.COLS - 1):
                if (i, j) not in self.banned:
                    self.grid[i][j] = self.__X

        return self.grid
