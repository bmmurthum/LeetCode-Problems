class Solution:
    """Problem by LeetCode.com"""

    def can_be_equal(self, target: list[int], arr: list[int]) -> bool:
        """
        With some amount of swapping values between positions, can these two
        lists become equal?

        Args:
            `target`: A first list
            `arr`: A second list
        Returns:
            `True/False`: Whether they could be equal after rearrange.
        """

        # Are they equal when sorted?
        target.sort()
        arr.sort()
        if target == arr:
            return True
        else:
            return False
