""" Module to find if there is a jumping path to the end index. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201
# Ignore the advise to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem given by LeetCode."""

    def can_jump(self, nums: list[int]) -> bool:
        """
        Looking at a list of values that represent how far further in the list
        you could jump to, is there a path to the last value?

        Args:
            `nums`: A list of how-far-can-jump values.
        Returns:
            `True/False`: Whether the last index can be reached.
        """

        # Create list of noting if an index is reachable.
        can_reach = [False] * len(nums)
        can_reach[0] = True

        # Look for reach
        for i in range(len(nums) - 1):
            if can_reach[i] is False:
                # This current value isn't reachable
                return False
            elif nums[i] != 0:
                if i + nums[i] >= len(nums) - 1:
                    # This value reaches last index
                    return True
                for j in range(i + 1, i + nums[i] + 1):
                    can_reach[j] = True
        return can_reach[-1]
