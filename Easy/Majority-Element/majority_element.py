""" Module to return the value of the element that is a majority of the items in a list. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def majority_element(self, nums: list[int]) -> int:
        """
        Returns the value of the items that are a majority of the items in the list.

        It's assumed that there is an item that this is the case.

        Args:
            `nums`: The given list to look through.
        Returns:
            `majority_item`: The value of the item of majority. `None` if no majority item.
        """
        nums_set = set(nums)
        for i in nums_set:
            if nums.count(i) > len(nums) // 2:
                return i

    def majority_element_2(self, nums: list[int]) -> int:
        """
        Returns the value of the items that are a majority of the items in the list.

        It's assumed that there is an item that this is the case.

        Args:
            `nums`: The given list to look through.
        Returns:
            `majority_item`: The value of the item of majority. `None` if no majority item.
        """

        count_to_pass = len(nums) // 2
        count_dict = {}
        for _, item in enumerate(nums):
            if count_dict.get(item) is None:
                count_dict[item] = 1
            else:
                count_dict[item] = count_dict[item] + 1
            if count_dict[item] > count_to_pass:
                return item
