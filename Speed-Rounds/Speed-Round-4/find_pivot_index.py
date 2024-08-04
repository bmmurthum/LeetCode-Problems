class Solution:
    """Problem provided by LeetCode"""

    def pivot_index(self, nums: list[int]) -> int:
        """
        Find an left-most index that has an equal sum to the left and right of
        this index.

        Args:
            `nums`: A list of integers
        Returns:
            `index`: An index that balances list sums on each side.
        """

        # 19 min

        # Fixes:
        # - Didn't account for negative values

        # Handle edge-cases
        length = len(nums)
        if length == 1:
            return 0
        if sum(nums[1:]) == 0:
            return 0
        if length == 2:
            return -1

        # Prep a list of totals from the right
        post_fix = [-1] * len(nums)
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            total += nums[i]
            post_fix[i] = total

        # If a total comes to be equal to a total from the post-fix list in a
        # correct placement, we know we have a balance point. If our total
        # becomes greater than post-fix values, we can stop early.
        total = 0
        for j in range(len(nums)):
            total += nums[j]
            if total == post_fix[j]:
                return j
        return -1
