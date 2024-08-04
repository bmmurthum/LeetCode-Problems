class Solution:
    """Problem provided by LeetCode"""

    def find_max_average(self, nums: list[int], k: int) -> float:
        """
        Finds the maximum average of neighboring values of a count of `k`
        neighbors.

        Args:
            `nums`: The list of integers.
            `k`: The length of considered neighbors.
        Returns:
            `max_average`: The maximum average found in a section within.
        """

        # 11 min

        # Fixes:
        # - Time limit exceeded. Changed from sum() on truncated lists to
        #   current.
        # - Overlooked values including negatives

        # Handle edge cases
        if len(nums) == 1:
            return float(nums[0])
        if k == 1:
            return float(max(nums))
        if k == len(nums):
            return float(sum(nums) / k)

        # Slide a window and keep track of largest.
        current_total = sum(nums[0:k])
        max_total = current_total
        for i in range(1, len(nums) - k + 1):
            current_total -= nums[i - 1]
            current_total += nums[i + k - 1]
            if current_total > max_total:
                max_total = current_total
        return max_total / k
