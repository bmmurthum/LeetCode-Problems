class Solution:
    """Problem from LeetCode.com"""

    def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:
        """
        Returns a particular chunk of the sum of all ranges within the given
        list.

        Args:
            `nums`: A list of positive integers.
            `n`: Length of the list.
            `left`: The left index of the generated list, to begin sum().
            `right`: The right index, to conclude the sum().
        Returns:
            `new_sum`: The sum of this portion of the generated list.
        """

        # Generate range sums.
        sub_array_sums = []
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                sub_array_sums.append(total)

        # Sort, find our sum, and return the result after applying mod.
        sub_array_sums.sort()
        new_sum = sum(sub_array_sums[left - 1 : right])
        new_sum = new_sum % (10**9 + 7)
        return new_sum
