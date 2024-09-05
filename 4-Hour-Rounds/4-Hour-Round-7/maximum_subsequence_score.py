"""Problem from LeetCode.com"""

# pylint: disable=C0200

import heapq


class Solution:
    """Problem from LeetCode.com"""

    def max_score(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Given two synced lists, we're trying to find the best collection of
        indices where we have `k` number of values. In `nums1` we sum those
        values, to then multiply by the minimum value of `nums2`. We're looking
        for the highest product possible between these lists.

        Args:
            `nums1`: A first list of non-negative integers.
            `nums2`: A second list of non-negative integers.
        Returns:
            `max_product`: A maximum found product.
        """

        def sort_the_lists(a: list[int], b: list[int]) -> list:
            """
            Sort the lists together with the second list being from largest to
            smallest.
            """
            # a = [4, 2, 3, 1, 1]
            # b = [7, 5, 10, 9, 6]
            # output = [[3, 10], [1, 9], [4, 7], [1, 6], [2, 5]]
            return [
                [x, y] for x, y in sorted(zip(a, b), key=lambda i: i[1], reverse=True)
            ]

        # Handle edge-case.
        # Avoids doing all the heap stuff and merging of lists on a large list
        # with k == 1
        if k == 1:
            max_product = 0
            for i in range(len(nums1)):
                temp = nums1[i] * nums2[i]
                if temp > max_product:
                    max_product = temp
            return max_product

        # Sort the lists.
        zipped = sort_the_lists(nums1, nums2)

        # Build an initial list of max-sum-values in a list.
        # Keep a note on the sum of that list, if it changes.
        max_product = 0
        max_values = []
        max_values_sum = 0
        for j in range(0, k - 1):
            heapq.heappush(max_values, zipped[j][0])
            max_values_sum += zipped[j][0]
        max_product = (zipped[k - 1][0] + sum(max_values)) * zipped[k - 1][1]

        # Iterate through the list generating best product as we go.
        for i in range(k, len(zipped)):
            heapq.heappush(max_values, zipped[i - 1][0])
            max_values_sum -= heapq.heappop(max_values)
            max_values_sum += zipped[i - 1][0]
            max_product = max(
                max_product, (zipped[i][0] + max_values_sum) * zipped[i][1]
            )
        return max_product
