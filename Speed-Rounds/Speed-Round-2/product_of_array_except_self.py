class Solution:
    """Problem provided by LeetCode"""

    def product_except_self(self, nums: list[int]) -> list[int]:
        """
        Returns a list of products all numbers in the given list except for the number at the `ith` position. Aim for O(n) time complexity.

        Args:
            `nums`: A list of integers
        Returns:
            `new_list`: A list of products
        """

        # To write it such that you multiply all, then divide your answer is so good, but unavailable.

        # 34 min

        # Had to look up prefix/suffix ideas
        # Looks like O(2n), which counts as O(n)

        # Create a list of a building total product
        prefix = []
        total = 1
        for item in nums:
            total *= item
            prefix.append(total)

        # Create a list of a building total product from the right
        suffix = [1] * len(nums)
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            total *= nums[i]
            suffix[i] = total

        # Our new list is created from portions of these lists
        new_list = [-1] * len(nums)
        new_list[0] = suffix[1]
        new_list[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            new_list[i] = prefix[i - 1] * suffix[i + 1]
        return new_list
