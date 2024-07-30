""" Module to find if a linked-list has any cycles. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def max_profit(self, prices: list[int]) -> int:
        """
        Looks for a best profit case between a buy and sell on known prices.

        Args:
            `prices`: A list of prices of a stock.
        Returns:
            `max_profit`: The best profit return that can be found.
        """

        # Handle edge case
        if len(prices) == 1:
            return 0

        # Look for largest difference whenever we find a new lowest-num
        temp_min = 10**4 + 1
        max_profit = 0
        for i, price in enumerate(prices[0:-1]):
            if price < temp_min:
                temp_min = price
                temp_best_profit = max(prices[i + 1 :]) - price
                if temp_best_profit > max_profit:
                    max_profit = temp_best_profit

        return max_profit
