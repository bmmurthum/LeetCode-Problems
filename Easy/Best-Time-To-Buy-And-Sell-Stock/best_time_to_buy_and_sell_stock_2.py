class Solution:

    def max_profit_2(self, prices: list[int]) -> int:
        l, n, mp = 0, len(prices), 0
        for i in range(1, n):
            l = i if prices[i] < prices[l] else l
            mp = max(prices[i] - prices[l], mp)
        return mp
