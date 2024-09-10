"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def max_profit(self, prices: list[int], fee: int) -> int:
        """
        Finds the max profit from trades given a list of prices on each day.
        With consideration that there's a fee on each trade.

        Args:
            `prices`: A list of price on each day.
            `fee`: The fee for a trade.
        Returns:
            `output`: The maximal profit from any trades.
        """

        # Find a first minimum.
        current_highest = prices[0]
        current_lowest = prices[0]
        start = 0
        for j in range(len(prices)):
            # val = prices[j]
            if prices[j] < current_highest:
                current_highest = prices[j]
                start = j
            if prices[j] > current_highest:
                start = j - 1
                break

        # Buy low, sell at local maxima determined with fee.
        current_highest = prices[start]
        current_lowest = prices[start]
        profit = 0
        for i in range(start, len(prices)):
            # val = prices[i]

            # Flow down to a local minimum.
            if current_highest == current_lowest and prices[i] < current_lowest:
                current_highest = prices[i]
                current_lowest = prices[i]
                continue

            # If at a local maximum accounting for fee.
            if (
                current_highest > prices[i] + fee
                and current_highest != current_lowest
                and current_highest - current_lowest > fee
            ):
                profit += current_highest - current_lowest - fee
                current_highest = prices[i]
                current_lowest = prices[i]

            # Update current maximums and minimums to record what to "buy" and
            # "sell".
            else:
                if prices[i] > current_highest and prices[i] - fee > current_lowest:
                    current_highest = prices[i]
                elif prices[i] < current_lowest:
                    current_lowest = prices[i]

        # Handle ending.
        if current_highest > current_lowest + fee:
            profit += current_highest - current_lowest - fee
        return profit
