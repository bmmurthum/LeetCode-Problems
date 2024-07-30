""" Module to find if a linked-list has any cycles. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def max_profit(self, prices: list[int]) -> int:
        """
        Looks for a best profit to be made with multiple buys and sell on a
        list of known prices.

        Args:
            `prices`: A list of prices of a stock.
        Returns:
            `max_profit`: The best profit return that can be found.
        """

        # Handle single item list case
        if len(prices) == 1:
            return 0

        # When the next one is higher, grab this
        # When the next one is lower, sell this
        bought = float("inf")
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1] and prices[i] < bought:
                bought = prices[i]
            elif prices[i] > prices[i + 1] and bought != float("inf"):
                profit += prices[i] - bought
                bought = float("inf")
        if bought != float("inf") and prices[-1] > bought:
            profit += prices[-1] - bought
        return profit
