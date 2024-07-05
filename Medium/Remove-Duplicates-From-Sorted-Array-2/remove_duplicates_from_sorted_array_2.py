""" Module to remove elements from a list if there are more than 2 of that value. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def remove_duplicates(self, nums: list[int]) -> int:
        """
        Removes elements from list, if there are more than 2 of that value. Keeps in relative order, handles in-place.

        If `b` items were removed, the list will be the same length, but with garbage values in the last `b` spaces.

        Args:
            `nums`: A list of integers. Sorted in non-decreasing order.
        Returns:
            `new_nums`: Now with removed items.
        """

        # Not possible changes to be made. Return.
        if len(nums) < 3:
            return len(nums)
        # Initial variables
        look_index = 0
        change_index = 0
        mx = 2
        current_num = nums[0]
        value_ct = 0
        # Walk through list with two pointers and some helper variables
        while look_index < len(nums):
            if nums[look_index] == current_num:
                value_ct += 1
            else:
                current_num = nums[look_index]
                value_ct = 1
            nums[change_index] = nums[look_index]
            if value_ct <= mx:
                change_index += 1
            look_index += 1
        return change_index
