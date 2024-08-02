""" Module to find the best gas-station to start at. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201
# Ignore the advise to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem by LeetCode.com"""

    def can_complete_circuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Find the gas station that will allow us to do a complete circuit.
        Returns `-1` if none are good.

        Args:
            `gas`: The amount of gas at a station.
            `cost`: The amount of gas to get to the next station.
        Returns:
            `possible_start`: The index of the station to start at.
        """

        # If the total gas is less than cost, there is no solution.
        if sum(gas) - sum(cost) < 0:
            return -1

        # For each station, "Have we run out of gas?"
        # "What if we started at the next one?"
        total_gas = 0
        possible_start = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            if total_gas < 0:
                total_gas = 0
                possible_start = i + 1
        return possible_start
