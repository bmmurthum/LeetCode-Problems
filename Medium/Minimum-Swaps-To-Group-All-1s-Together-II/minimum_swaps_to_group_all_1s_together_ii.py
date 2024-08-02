class Solution:
    """Problem by LeetCode.com"""

    def min_swaps(self, nums: list[int]) -> int:
        """
        Returns the minimum number of position swaps to have all 1s next to one
        another in a row. The list is imagined at both ends being connected.

        Args:
            `nums`: A list of 1s and 0s.
        Return:
            `swaps_needed`: A number of swaps.
        """

        # Handle 1-item case.
        if len(nums) == 1:
            return 0

        # Find a size of a sliding window.
        # A window that could fit all 1s.
        window_size = 0
        for value in nums:
            if value == 1:
                window_size += 1

        # Handle single 1 case.
        if window_size == 1:
            return 0

        # Handle grouped from beginning moment.
        looped_nums = nums + nums
        count = looped_nums[0 : 0 + window_size].count(1)
        if count == window_size:
            return 0

        # Find a moment with the most 1s inside the window.
        max_count = -1
        for i in range(1, len(nums)):
            if looped_nums[i + window_size - 1] == 1:
                count += 1
            if looped_nums[i - 1] == 1:
                count -= 1
            if count > max_count:
                max_count = count

        # The number of swaps needed ends up being equal to the number of
        # zeroes inside this window.
        swaps_needed = window_size - max_count
        return swaps_needed
