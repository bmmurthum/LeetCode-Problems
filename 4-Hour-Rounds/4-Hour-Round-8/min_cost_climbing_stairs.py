"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def min_cost_climbing_stairs(self, cost: list[int]) -> int:
        """
        To climb a stair, you must pay the cost at cost[i]. Upon paying that
        cost, we can step two forward, or one. What's the minimum cost to reach
        the last step?

        t0 = 1, t1 = 5, tn = min(tn-1,tn-2) + tn

        Args:
            `cost`: A list of costs to use this stair.
        Returns:
            `output`: The minimum cost to reach the top stair.
        """

        # Edge-case: Two stairs
        if len(cost) == 2:
            return min(cost)
        # Edge-case: Three stairs
        if len(cost) == 3:
            return min((cost[0] + cost[2]), cost[1])

        # Calculate min-cost as we iterate through the list, using a
        # dynamic-programming approach.
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]

        # The last two steps hold the possible costs to reach the
        # end. Return the minimum of these.
        output = min(cost[-1], cost[-2])
        return output
