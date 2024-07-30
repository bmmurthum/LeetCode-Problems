class Solution:
    def max_profit_3(self, prices: list[int]) -> int:
        max_profit = 0
        current_buy_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > current_buy_price:
                max_profit += prices[i] - current_buy_price
            current_buy_price = prices[i]
        return max_profit
