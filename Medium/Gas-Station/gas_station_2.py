class Solution:

    def can_complete_circuit_2(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        cur_gas, ans = 0, 0
        for i in range(len(cost)):
            if cur_gas < 0:
                ans = i
                cur_gas = gas[i] - cost[i]
            else:
                cur_gas += gas[i]
                cur_gas -= cost[i]

        return ans
