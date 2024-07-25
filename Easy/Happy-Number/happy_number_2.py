class Solution:
    def is_happy_2(self, n: int) -> bool:
        g = set()
        while n != 1:
            sqarsum = 0
            for i in str(n):
                sqarsum += int(i) ** 2
            n = sqarsum
            if n in g:
                return False
            else:
                g.add(n)
        return True
