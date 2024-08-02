import numpy as np


class Solution:

    def can_complete_circuit_4(self, gas: list[int], cost: list[int]) -> int:
        diff = np.array(gas) - np.array(cost)
        i = 0
        while i < len(diff):
            con = np.concatenate([diff[i:], diff[:i]])
            cum_sum = np.cumsum(con)
            if cum_sum.min() >= 0:
                return i
            i = cum_sum.argmin() + 1 + i
        return -1
