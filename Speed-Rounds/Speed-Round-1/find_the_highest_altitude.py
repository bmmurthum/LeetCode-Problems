class Solution:
    """Problem provided by LeetCode"""

    def largest_altitude(self, gain: list[int]) -> int:
        """
        Finds the highest altitude of a hiker. The given list represents
        differences in altitude at different checkpoints.

        Args:
            `gain`: The difference of altitude from the last checkpoint.
        """

        # 3 min, 50 sec.

        current_alt = 0
        highest_alt = 0
        for diff in gain:
            current_alt += diff
            if current_alt > highest_alt:
                highest_alt = current_alt
        return highest_alt
