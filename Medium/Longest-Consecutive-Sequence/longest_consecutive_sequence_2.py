from collections import defaultdict


class Solution:
    def longest_consecutive_2(self, nums: list[int]) -> int:
        x = set(nums)
        lk = defaultdict(int)
        visited = set()
        result = 0
        for n in x:
            if n in visited:
                continue
            if n - 1 in x:
                continue
            visited.add(n)
            l = 1
            original_n = n
            while (n := n + 1) in x:
                l += 1
                visited.add(n)
            l += lk[original_n - 1]
            lk[n - 1] = l
            result = max(result, l)
        return result
