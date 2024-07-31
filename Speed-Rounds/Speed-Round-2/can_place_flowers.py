class Solution:
    """Problem provided by LeetCode"""

    def can_place_flowers(self, flower_bed: list[int], n: int) -> bool:
        """
        Tells us if we can place a number of flowers into this flower bed. Each
        flower must have one space between them.

        Args:
            `flower_bed`: The list of whether there is currently a flower
                planted.
            `n`: The number of flowers we intend to plant.
        """

        # 7 min 25 sec

        # Check if a given spot is valid to put plant.
        for i, is_taken in enumerate(flower_bed):

            # Does the area to the left have a plant?
            left = False
            if i == 0:
                left = False
            elif flower_bed[i - 1] == 1:
                left = True
                continue

            # Does the area to the right have a plant?
            right = False
            if i == len(flower_bed) - 1:
                right = False
            elif flower_bed[i + 1] == 1:
                right = True
                continue

            # Plant a plant!
            if is_taken == 0 and right is False and left is False:
                n -= 1
                flower_bed[i] = 1

        # If we've planted them all, success.
        if n <= 0:
            return True
        return False
