""" Module to look for number of mutation-differences between two gene-strings. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201

from collections import deque


class Solution:
    """Problem given by LeetCode."""

    def min_mutation(self, start_gene: str, end_gene: str, bank: list[str]) -> int:
        """
        Returns the number of mutations needed to change the beginning
        gene-string to the ending gene-string.

        Args:
            `start_gene`: The starting gene-string.
            `end_gene`: The end gene-string that we desire.
            `bank`: A list of valid genes that give options of mutations.
        Returns:
            `mutation_count`: The number of steps to get to final gene-string.
                Returns `-1` if the final gene-string is unable to be reached.
        """
        # Mutations that have been visited
        visited = []
        visited.append(start_gene)

        # Which mutations to look at next
        queue = deque()
        next_queue = deque()
        queue.append(start_gene)

        # Breadth-first search
        mutation_count = 0
        while queue:
            current = queue.popleft()
            # Stop when found goal.
            if current == end_gene:
                return mutation_count
            # Consider which positions to look at next.
            for _, item in enumerate(bank):
                if self.is_one_char_diff(current, item) and item not in visited:
                    next_queue.append(item)
                    visited.append(item)
            # Set up next steps in queue
            if len(queue) == 0:
                queue = next_queue.copy()
                next_queue.clear()
                mutation_count += 1

        # If never bumped into goal, return -1
        return -1

    def is_one_char_diff(self, a: str, b: str) -> bool:
        """
        Checks to see that the two given strings only have one character
        difference. It requires that the two strings are the same length.

        Args:
            `a`: First string.
            `b`: Second string.
        Returns:
            `True/False`: If there is only one character difference.
        """
        count = 0
        for x, y in zip(a, b):
            if x != y:
                count += 1
        if count == 1:
            return True
        else:
            return False
