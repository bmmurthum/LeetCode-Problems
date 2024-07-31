class Solution:
    """Problem provided by LeetCode"""

    def increasing_triplet_2(self, nums: list[int]) -> bool:
        """
        Returns whether there exists an increasing triplet to be found within
        the list, disregarding the space between the items.

        Args:
            `nums`: The list of integers.
        Returns:
            `True/False`: Whether a valid triplet was found.
        """

        # 25 min before submitting a failing solution with two pointers that
        # move inward.

        # This solution kind of looking like dynamic programming?
        # Prefix/suffix?

        # Create a list of "minimum to this point" from the left.
        minimums = [None] * len(nums)
        new_min = nums[0]
        for i, value in enumerate(nums):
            if value < new_min:
                new_min = value
            minimums[i] = new_min

        # Create a list of "maximum to this point" from the right.
        maximums = [None] * len(nums)
        new_max = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > new_max:
                new_max = nums[i]
            maximums[i] = new_max

        # At any point, is there a minimum to my left that is lower and a max
        # to the right that is higher?
        for i in range(1, len(nums) - 1):
            if minimums[i - 1] < nums[i] and maximums[i + 1] > nums[i]:
                return True
        return False
