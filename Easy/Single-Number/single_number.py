"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def single_number(self, nums: list[int]) -> int:
        """
        The given list contains duplicates of numbers except for a single case
        of one number. Find that number. Try to do this in linear time.

        Args:
            `nums`: A given list of mostly duplicates.
        Returns:
            `output`: The single value.
        """

        bit_container = 0
        for num in nums:
            bit_container = bit_container ^ num
        return bit_container
