""" Someone else's solution. """

from collections import deque


class Solution:

    def min_mutation_3(self, startGene: str, endGene: str, bank: list[str]) -> int:
        def checkNeighbor(a, b):
            return sum([1 for i in range(len(a)) if a[i] != b[i]]) == 1

        q = deque([[startGene, 0]])
        visited = {startGene}
        while q:
            curr, mutation = q.popleft()
            if curr == endGene:
                return mutation

            for nei in bank:
                if checkNeighbor(curr, nei) and nei not in visited:
                    q.append([nei, mutation + 1])
                    visited.add(nei)

        return -1
