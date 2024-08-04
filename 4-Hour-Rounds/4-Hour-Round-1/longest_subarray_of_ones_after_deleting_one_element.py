"""Problem from LeetCode.com"""

# Ignore the advice to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def longest_subarray(self, nums: list[int]) -> int:
        """
        If we must delete one item from the list, what will be the longest
        number of consecutive ones in the list?

        Args:
            `nums`: A list of ones and zeroes.
        Returns:
            `max_length`: Size of the longest chain of ones.
        """

        # Handle edge cases
        # - If all ones or all zeroes
        # - If length of 1 & 2
        # - If only one 1
        total_sum = sum(nums)
        if len(nums) == total_sum:
            return total_sum - 1
        if total_sum == 0:
            return 0
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if total_sum > 0:
                return 1
            return 0
        if total_sum == 1:
            return 1

        max_length = 0

        # Pre-fix
        current = 0
        prefix_list = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                prefix_list[i] = current
                if current > max_length:
                    max_length = current
            else:
                current = 0
                prefix_list[i] = current

        # Post-fix
        current = 0
        postfix_list = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 1:
                current += 1
                postfix_list[i] = current
                if current > max_length:
                    max_length = current
            else:
                current = 0
                postfix_list[i] = current

        # Find a max chain of ones by looking at the lengths of chains before
        # and after the current position.

        for i in range(1, len(nums) - 1):
            if prefix_list[i - 1] + postfix_list[i + 1] > max_length:
                max_length = prefix_list[i - 1] + postfix_list[i + 1]
        return max_length
