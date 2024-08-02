class Solution:
    def can_complete_circuit_3(self, gas: list[int], cost: list[int]) -> int:
        c = 0
        d = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(d) < 0:
            return -1
        if len(d) == 1:
            return 0
        i = 0
        k = 0
        t = 0
        j = 0
        while i < len(d):
            k = k + d[j]
            t = j
            j = (j + 1) % len(d)
            if k < 0:
                k = 0
                i = -1
            i += 1
        if k >= 0:
            return j
        else:
            return -1
