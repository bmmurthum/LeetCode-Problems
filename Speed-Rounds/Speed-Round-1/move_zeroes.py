class Solution:
    """Problem provided by LeetCode"""

    def move_zeroes(self, nums: list[int]) -> None:
        """
        Moves any non-zero integers in the list to the left, keeping order.
        Zeroes are placed to the right. Does this in-place.

        Args:
            `nums`: A list of integers.
        """

        # 13 min

        # Fixed after
        # for _, item in enumerate(nums):
        #  - enumerate() returns a tuple
        # for i in range(left, len(nums)):
        #     nums[i] = 0
        #  - `left` is the start position in this range() call

        # Move a pointer to be at the position in which new numbers should be
        # placed. This number `left` is equal to how many NOT-ZEROS were found.
        # As iterating through, place numbers to that position.
        left = 0
        for _, item in enumerate(nums):
            if item != 0:
                nums[left] = item
                left += 1

        # Replace left over numbers at end of `nums` with zeroes.
        for i in range(left, len(nums)):
            nums[i] = 0
