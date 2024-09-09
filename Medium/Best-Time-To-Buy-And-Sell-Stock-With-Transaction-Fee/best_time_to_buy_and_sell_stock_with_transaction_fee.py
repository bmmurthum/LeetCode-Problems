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

            # Update current maximums and minimums to record "buy" and "sell".
            else:
                if prices[i] > current_highest:
                    current_highest = prices[i]
                elif prices[i] < current_lowest:
                    current_lowest = prices[i]

        # Handle ending.
        if current_highest > current_lowest + fee:
            profit += current_highest - current_lowest - fee
        return profit

    def max_profit_4(self, prices: list[int], fee: int) -> int:
        """
        Finds the max profit from trades given a list of prices on each day.
        With consideration that there's a fee on each trade.

        Args:
            `prices`: A list of price on each day.
            `fee`: The fee for a trade.
        Returns:
            `output`: The maximal profit from any trades.
        """

        # With a 2D grid we're keeping a note of previously made profit, and
        # considering if a sell would add more profit than other sells to keep
        # a log of the max as we iterate through.

        # prices = [1, 3, 2, 8, 4, 9]
        # fee = 0
        #            1  3  2  8  4  9
        # grid = 1 [[0, 2, 2, 7, 7, 8],
        #        3  [0, 2, 2, 7, 7, 8],
        #        2  [0, 2, 2, 8, 8, 9],
        #        8  [0, 2, 2, 8, 8, 9],
        #        4  [0, 2, 2, 8, 8, 13],
        #        9  [0, 2, 2, 8, 8, 13]]

        # At grid[2][3], looking at 2 and 8, we can see the 2 to the left of
        # our position is 2 indicating the sale of (3-1) having been done. If
        # we sell our current 2 at price 8, we'd add the (8-2) to the 2 from
        # before to take this position to 8 total. If this 8 is greater than
        # the above number or left number we set it as 8.

        # To use less memory (imagine a 2D list being 50,000 ^ 2 items), we can
        # look at the last layer of this grid as `memory` while we update this
        # list to be the current layer. This also reduces any time in copying
        # long lists.

        # Initialize a list for keeping log of "last" layer.
        memory = [0 for _ in range(len(prices))]

        # Setup initial memory.
        for i in range(1, len(prices)):
            memory[i] = max(
                prices[i] - prices[0] - fee,
                memory[i - 1],
            )

        # Calculate a new layer based on some info from the last.
        for y in range(1, len(prices)):
            previous_sells = memory[y]
            for i in range(y + 1, len(prices)):
                memory[i] = max(
                    [
                        prices[i] - prices[y] - fee + previous_sells,  # new
                        memory[i - 1],  # last option to left
                        memory[i],  # layer above
                    ]
                )

        # Return the last value.
        output = memory[-1]
        return output

    def max_profit_3(self, prices: list[int], fee: int) -> int:
        """
        Finds the max profit from trades given a list of prices on each day.
        With consideration that there's a fee on each trade.

        Args:
            `prices`: A list of price on each day.
            `fee`: The fee for a trade.
        Returns:
            `output`: The maximal profit from any trades.
        """

        # TODO - This gave us a time-limit-exceeded.

        # With a 2D grid we're keeping a note of previously made profit, and
        # considering if a sell would add more profit than other sells to keep
        # a log of the max as we iterate through.

        # prices = [1, 3, 2, 8, 4, 9]
        # fee = 0
        #            1  3  2  8  4  9
        # grid = 1 [[0, 2, 2, 7, 7, 8],
        #        3  [0, 2, 2, 7, 7, 8],
        #        2  [0, 2, 2, 8, 8, 9],
        #        8  [0, 2, 2, 8, 8, 9],
        #        4  [0, 2, 2, 8, 8, 13],
        #        9  [0, 2, 2, 8, 8, 13]]

        # At grid[2][3], looking at 2 and 8, we can see the 2 to the left of
        # our position is 2 indicating the sale of (3-1) having been done. If
        # we sell our current 2 at price 8, we'd add the (8-2) to the 2 from
        # before to take this position to 8 total. If this 8 is greater than
        # the above number or left number we set it as 8.

        # To use less memory (imagine a list of 50,000 ^ 2), we're looking at
        # only the last two layers of this grid at any point in time.

        # Initialize a simple 2 layer grid with all zeroes.
        grid = [[0 for _ in range(len(prices))] for _ in range(2)]

        # Setup first layer.
        for i in range(len(prices)):
            grid[0][i] = max(
                prices[i] - prices[0] - fee,
                grid[0][i - 1],
            )

        # Calculate a new layer based on some info from the last.
        for y in range(1, len(prices)):
            grid[1] = grid[0].copy()
            previous_sells = grid[1][y]
            for i in range(y + 1, len(prices)):
                grid[1][i] = max(
                    [
                        prices[i] - prices[y] - fee + previous_sells,
                        grid[1][i - 1],
                        grid[0][i],
                    ]
                )
            grid[0] = grid[1]

        # Return the value of the bottom right corner.
        output = grid[1][-1]
        return output

    def max_profit_2(self, prices: list[int], fee: int) -> int:
        """
        Finds the max profit from trades given a list of prices on each day.
        With consideration that there's a fee on each trade.

        Args:
            `prices`: A list of price on each day.
            `fee`: The fee for a trade.
        Returns:
            `output`: The maximal profit from any trades.
        """

        # TODO - This gave us a memory-limit-exceeded.

        # With a 2D grid we're keeping a note of previously made profit, and
        # considering if a sell would add more profit than other sells to keep
        # a log of the max as we iterate through.

        # prices = [1, 3, 2, 8, 4, 9]
        # fee = 0
        #            1  3  2  8  4  9
        # grid = 1 [[0, 2, 2, 7, 7, 8],
        #        3  [0, 2, 2, 7, 7, 8],
        #        2  [0, 2, 2, 8, 8, 9],
        #        8  [0, 2, 2, 8, 8, 9],
        #        4  [0, 2, 2, 8, 8, 13],
        #        9  [0, 2, 2, 8, 8, 13]]
        #
        # At grid[2][3], looking at 2 and 8, we can see the 2 to the left of
        # our position is 2 indicating the sale of (3-1) having been done. If
        # we sell our current 2 at price 8, we'd add the (8-2) to the 2 from
        # before to take this position to 8 total. If this 8 is greater than
        # the above number or left number we set it as 8.

        # Initialize a grid with all zeroes.
        grid = [[0 for _ in range(len(prices))] for _ in range(len(prices))]
        for y in range(len(prices)):
            if y > 0:
                grid[y] = grid[y - 1].copy()
            previous_sells = grid[y][y]
            for i in range(y + 1, len(prices)):
                grid[y][i] = max(
                    [
                        prices[i] - prices[y] - fee + previous_sells,
                        grid[y][i - 1],
                        grid[y - 1][i],
                    ]
                )

        # Return the value of the bottom right corner.
        output = grid[len(grid) - 1][len(grid[0]) - 1]
        return output


# prices = [1, 3, 2, 8, 4, 9]
# fee = 2
# correct = 8
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# prices = [1, 3, 7, 5, 10, 3]
# fee = 3
# correct = 6
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# prices = [1, 3, 2, 8, 4, 9]
# fee = 0
# correct = 13
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# prices = [1, 3, 7, 3, 5, 8]
# fee = 3
# correct = 5
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# prices = [1, 3, 7, 4, 10, 3]
# fee = 3
# correct = 6
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# prices = [1, 3, 7, 4, 10, 11]
# fee = 3
# correct = 7
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# prices = [1, 3, 7, 4, 10, 11]
# fee = 3
# correct = 7
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# prices = [1, 10, 8, 5, 1, 3, 6]
# fee = 3
# correct = 8
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# Fixed an issue with accounting for finding a first starting buy-in.
# prices = [
#     37416,
#     15836,
#     27200,
#     6624,
#     47529,
#     36404,
#     100,
#     34636,
#     39871,
#     8624,
#     32317,
#     15232,
# ]
# fee = 6806
# correct = 88509
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# Fixed an issue with finding local minimums.
# prices = [
#     35823,
#     49431,
#     5215,
#     41907,
#     31923,
#     26514,
#     13188,
#     14880,
#     21567,
#     37416,
#     15836,
#     27200,
# ]
# fee = 6806
# correct = 58668
# result = Solution().max_profit(prices, fee)
# if correct == result:
#     print("Correct")
# else:
#     print(f"Failure. Result: {result}")

# Fixed an issue not accounting for a difference in fee.
prices = [
    35497,
    34155,
    42090,
    41991,
    18605,
    23116,
    16109,
    45554,
    5501,
    30145,
    2488,
    10848,
    30203,
    13151,
    7037,
    28633,
    7150,
]
fee = 6806
correct = 77305
result = Solution().max_profit(prices, fee)
if correct == result:
    print("Correct")
else:
    print(f"Failure. Result: {result}")
