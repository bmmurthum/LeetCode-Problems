""" Someone else's solution. """

from collections import deque


class Solution:
    def min_mutation_2(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)
        choices = ["A", "C", "T", "G"]

        q = deque([startGene])
        seen = {startGene}
        mutations = 0

        def neighbors(s):
            # input is a list s of characters
            neighbors = []
            for i in range(len(s)):
                for choice in choices:
                    if s[i] == choice:
                        continue
                    neighbor = s[:i] + choice + s[i + 1 :]
                    # a gene must be in bank to be valid
                    if neighbor in bank:
                        neighbors.append(neighbor)
            return neighbors

        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if node == endGene:
                    return mutations
                for neighbor in neighbors(node):
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append(neighbor)
            mutations += 1

        return -1
