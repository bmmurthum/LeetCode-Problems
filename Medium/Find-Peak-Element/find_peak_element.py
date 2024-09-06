"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def find_peak_element(self, nums: list[int]) -> int:
        """
        Find an index of an element that is strictly greater than its
        neighbors, a local maximum. Imagined values outside of the list are
        seen as infinitely low.

        Our list `nums` is guaranteed to have each neighbor value be distinct
        from another.

        Args:
            `nums`: A list integer values.
        Returns:
            `mid`: An index of a "peak" element, local maximum.
        """

        # Edge-cases:
        # - One item
        # - Two items
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 1
            return 0

        # We're looking for a local maximum by moving around "upward". Any
        # values outside of the list are imagined at low-values, which aids in
        # our search.

        # Doing a binary search with the condition of going towards a higher
        # value of the neighbors of the current value. A local-maximum would be
        # uphill, so we look to that new half.
        low = 0
        high = len(nums) - 1
        mid = None
        while low <= high:
            mid = (high + low) // 2

            # If at right edge and success.
            if mid == len(nums) - 1 and nums[mid - 1] < nums[mid]:
                return mid

            # If at left edge and success.
            if mid == 0 and nums[mid + 1] < nums[mid]:
                return mid

            # If in middle and success.
            if not (mid == len(nums) - 1 or mid == 0):
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid

            # If no success yet, do move.
            if mid == len(nums) - 1:
                high = mid - 1
            elif mid == 0:
                low = mid + 1
            elif nums[mid - 1] <= nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        return mid
