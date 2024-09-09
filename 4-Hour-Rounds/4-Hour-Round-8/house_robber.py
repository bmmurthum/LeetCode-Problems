"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def rob(self, nums: list[int]) -> int:
        """
        We're asked to rob the most amount of money from houses with each house
        having nums[i] cash. If we rob to adjacent houses, the police are
        called. This function returns the most money that can be robbed in a
        single night.

        t0 = 1, t1 = 5, tn = min(tn-1,tn-2) + tn

        Args:
            `nums`: A list of money stashes at each house.
        Returns:
            `output`: The maximum amount of money that can be stolen.
        """

        # Edge-case: One house
        if len(nums) == 1:
            return nums[0]
        # Edge-case: Two houses
        if len(nums) == 2:
            return max(nums)
        # Edge-case: Three houses
        if len(nums) == 3:
            return max((nums[0] + nums[2]), nums[1])

        # Dynamic-programming approach to finding total at any house.
        # Starting at the fourth house, look back at two-back and
        # three-back's total stolen sum and add that to the current value.
        nums[2] = nums[2] + nums[0]
        for i in range(3, len(nums)):
            nums[i] = nums[i] + max(nums[i - 2], nums[i - 3])

        # The last two totals are the two possible maximums. Return the max().
        output = max(nums[-1], nums[-2])
        return output
