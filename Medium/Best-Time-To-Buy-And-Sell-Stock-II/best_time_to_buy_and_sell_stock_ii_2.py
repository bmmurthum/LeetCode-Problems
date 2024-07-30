class Solution:
    def max_profit_2(self, prices: list[int]) -> int:
        # buy stock at valley, then sell at next peak
        running_profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] > prices[i]:
                running_profit += prices[i + 1] - prices[i]

        return running_profit
