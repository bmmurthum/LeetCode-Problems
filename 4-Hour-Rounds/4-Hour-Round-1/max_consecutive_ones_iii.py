"""Problem from LeetCode.com"""

# Ignore the advice to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def longest_ones(self, nums: list[int], k: int) -> int:
        """
        Knowing that we can flip `k` zeroes to ones, what's the longest chain
        of 1's we can find inside `nums`?

        Args:
            `nums`: Our list of ones and zeroes.
            `k`: How many zeroes we can flip.
        Returns:
            `longest_count`: A longest chain of ones, we could find.
        """

        # Handle edge cases
        # - All ones/zeroes
        # - Can flip all numbers
        # - List of size one/two
        sum_total = sum(nums)
        if k == len(nums):
            return k
        if sum_total == 0:
            return 0
        if sum_total == len(nums):
            return sum_total
        if len(nums) == 2 and k == 0:
            return sum_total
        elif len(nums) == 2 and k == 1:
            return sum_total + 1

        # Count from first-index, for a minimum.
        # - If reach end of nums without break, return early.
        longest_count = 0
        zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            if zeroes == k + 1:
                longest_count = i
                break
        if zeroes <= k:
            return len(nums)

        # Count from right, for edge case.
        zeroes = 0
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                zeroes += 1
            if zeroes == k + 1:
                if count > longest_count:
                    longest_count = count
                break
            count += 1

        # Starting with the left_ptr at any first one in a series, move the
        # right_ptr from there as far as possible while counting ones. If this
        # is a new max, store it.

        # On the right pointer reaching the end, we can stop iterating.
        left_ptr = 1
        right_ptr = 1
        reached_end = False
        while left_ptr < len(nums) - 1:
            if nums[left_ptr] == 1 and nums[left_ptr - 1] == 0:
                zeroes = 0
                ones = 1
                right_ptr = left_ptr + 1
                while zeroes <= k and not reached_end:
                    if nums[right_ptr] == 0:
                        zeroes += 1
                    else:
                        ones += 1
                    right_ptr += 1
                    if right_ptr >= len(nums):
                        reached_end = True
                if ones + zeroes - 1 > longest_count:
                    longest_count = ones + zeroes - 1
            if reached_end:
                break
            left_ptr += 1

        # Return the longest found.
        return longest_count
