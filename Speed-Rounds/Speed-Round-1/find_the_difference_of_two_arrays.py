class Solution:
    """Problem provided by LeetCode"""

    def find_difference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """
        Finds two lists of which distinct numbers are not within the other list.

        Args:
            `nums1`: First list of numbers.
            `nums2`: Second list of numbers.
        Returns:
            `d1`: Numbers only found in the first list.
            `d2`: Numbers only found in the second list.
        """

        # 5 min, 45 sec.

        # Set of distinct values.
        # Also allows us to check inside at hash speed.
        s_1 = set(nums1)
        s_2 = set(nums2)

        # Add to the lists if a value is in one but not the other.
        d_1 = []
        d_2 = []
        for item in s_1:
            if item not in s_2:
                d_1.append(item)
        for item in s_2:
            if item not in s_1:
                d_2.append(item)

        return [d_1, d_2]
