class Solution:
    """Problem provided by LeetCode"""

    def max_operations(self, nums: list[int], k: int) -> int:
        """
        Looks for pairs of numbers within `nums` that add to `k`. Count how
        many.

        Args:
            `nums`: The list of integers.
            `k`: The sum to look for.
        Returns:
            `total_removes`: The total number of pairs that sum to `k` to
            remove.
        """

        # 14 min

        # Fixes:
        # - Had to explore new pattern. Time limit exceeded.

        # Two pointers at each end of a sorted list. Move the pointers based on
        # their summed values.
        nums.sort()
        total_removes = 0
        left_ptr = 0
        right_ptr = len(nums) - 1
        while left_ptr < right_ptr:
            if nums[left_ptr] + nums[right_ptr] == k:
                total_removes += 1
                left_ptr += 1
                right_ptr -= 1
            elif nums[left_ptr] + nums[right_ptr] > k:
                right_ptr -= 1
            else:
                left_ptr += 1
        return total_removes
