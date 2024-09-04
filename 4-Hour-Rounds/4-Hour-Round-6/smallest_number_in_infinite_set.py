"""Problem from LeetCode.com"""

# pylint: disable=C0200

import heapq


class SmallestInfiniteSet:
    """Implement this class from LeetCode.com"""

    def __init__(self):
        """
        Initialize our "set" to contain all positive integers. Requirements
        dictate 1000 long memory.
        """
        self.nums = [i + 1 for i in range(1000)]
        self.nums_set = set(self.nums)
        heapq.heapify(self.nums)

    def pop_smallest(self) -> int:
        """
        Pop and return the smallest integer within our set.

        Returns:
            `removed`: Our smallest element, now removed.
        """
        removed = heapq.heappop(self.nums)
        self.nums_set.remove(removed)
        return removed

    def add_back(self, num: int) -> None:
        """
        Add an integer back into the set, if it has been removed.

        Args:
            `num`: Our number to add back into the set.
        """
        if num not in self.nums_set:
            heapq.heappush(self.nums, num)
            self.nums_set.add(num)
