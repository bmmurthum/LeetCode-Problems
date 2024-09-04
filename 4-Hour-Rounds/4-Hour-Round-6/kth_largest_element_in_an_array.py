"""Problem from LeetCode.com"""

# pylint: disable=C0200

import heapq


class Solution:
    """Problem from LeetCode.com"""

    def find_kth_largest(self, nums: list[int], k: int) -> int:
        """
        Given an array `nums`, find the kth largest element.

        Args:
            `nums`: An unsorted list of integers.
            `k`: Find the kth largest item.
        Returns:
            `output`: The integer value of the kth largest int.
        """

        # Using a heap to quickly store the values, and pop off.
        # Minimizing the length of the heap with the known k.
        temp = []
        count = 0
        for item in nums:
            if count <= k:
                heapq.heappush(temp, item)
                count += 1
            else:
                heapq.heappushpop(temp, item)
        output = heapq.nlargest(k, temp)
        return output[k - 1]
