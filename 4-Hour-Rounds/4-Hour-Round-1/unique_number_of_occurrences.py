"""Problem from LeetCode.com"""

# Ignore the advice to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def unique_occurrences(self, arr: list[int]) -> bool:
        """
        Each integer value in our list may occur any amount of times. Are there
        any two values that have the same amount of occurrences?

        Args:
            `arr`: Our list to check through.
        Returns:
            `True/False`: Whether there are two values with same quantity.
        """

        # Set up a dictionary for counts of unique values.
        arr_set = set(arr)
        count_dict = {}
        for item in arr_set:
            count_dict[item] = 0

        # Count quantity of each unique value.
        for _, item in enumerate(arr):
            count_dict[item] += 1
        values_list = count_dict.values()
        values_set = set(values_list)

        # If the number of unique counts is smaller than unique values, we can
        # know that there was a duplicate in the counts.
        if len(arr_set) == len(values_set):
            return True
        else:
            return False
