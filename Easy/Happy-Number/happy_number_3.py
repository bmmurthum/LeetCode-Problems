class Solution:
    def is_happy_3(self, n: int) -> bool:
        m = dict()
        while n != 1:
            if n in m:
                return False
            m[n] = 1
            n = sum([int(x) ** 2 for x in str(n)])
        return True
