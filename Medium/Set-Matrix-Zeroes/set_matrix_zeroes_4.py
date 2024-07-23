class Solution:
    def set_zeroes_4(self, a: list[list[int]]) -> None:
        b = [False] * len(a)
        c = [False] * len(a[0])
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 0:
                    b[i] = True
                    c[j] = True
        for i in range(len(b)):
            if b[i]:
                for j in range(len(a[0])):
                    a[i][j] = 0
        for i in range(len(c)):
            if c[i]:
                for j in range(len(a)):
                    a[j][i] = 0
