""" Module to find if there is two identical numbers near each other. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def contains_nearby_duplicate_a(self, nums: list[int], k: int) -> bool:
        """
        Tells us if there exists a particular number twice within a window `k`
        inside of `nums`.

        Args:
            `nums`: The list of numbers to look through.
            `k`: The max distance between any two identical numbers.
        Returns:
            `True/False`: If there is two of a single number within a distance
                `k` from one another inside the list.
        """

        # Remove edge-case.
        if k == 0:
            return False
        # If k is longer than our list, look at the whole list.
        length = len(nums)
        if k >= length - 1 and length != len(set(nums)):
            return True
        # If k is shorter than list, slide a window.
        else:
            for a in range(length - k):
                if len(set(nums[a : a + k + 1])) - 1 != k:
                    return True
        return False

    def contains_nearby_duplicate_b(self, nums: list[int], k: int) -> bool:
        """
        Tells us if there exists a particular number twice within a window `k`
        inside of `nums`.

        Args:
            `nums`: The list of numbers to look through.
            `k`: The max distance between any two identical numbers.
        Returns:
            `True/False`: If there is two of a single number within a distance
                `k` from one another inside the list.
        """

        # Remove edge-case.
        if k == 0:
            return False
        # If k is longer than our list, look at the whole list.
        length = len(nums)
        if k >= length - 1 and length != len(set(nums)):
            return True
        # If k is shorter than list, slide a window.
        else:
            for a in range(length - k):
                if nums[a] in set(nums[a + 1 : a + k + 1]):
                    return True
        return False

    def contains_nearby_duplicate_c(self, nums: list[int], k: int) -> bool:
        """
        Tells us if there exists a particular number twice within a window `k`
        inside of `nums`.

        Args:
            `nums`: The list of numbers to look through.
            `k`: The max distance between any two identical numbers.
        Returns:
            `True/False`: If there is two of a single number within a distance
                `k` from one another inside the list.
        """

        # Remove edge-case.
        if k == 0:
            return False
        # If k is longer than our list, look at the whole list.
        length = len(nums)
        if k >= length - 1 and length != len(set(nums)):
            return True
        # If k is shorter than list, check each item having a neighbor that is
        # close.
        else:
            for item in set(nums):
                a = nums.index(item)
                while a + k < length:
                    try:
                        if nums[a] in set(nums[a + 1 : a + k + 1]):
                            return True
                        a = nums.index(item, a + 1)
                    except:
                        break
        return False

    def contains_nearby_duplicate_d(self, nums: list[int], k: int) -> bool:
        """
        Tells us if there exists a particular number twice within a window `k`
        inside of `nums`.

        Args:
            `nums`: The list of numbers to look through.
            `k`: The max distance between any two identical numbers.
        Returns:
            `True/False`: If there is two of a single number within a distance
                `k` from one another inside the list.
        """

        # Remove edge-case.
        if k == 0:
            return False
        # If k is longer than our list, look at the whole list.
        length = len(nums)
        if k >= length - 1:
            if length != len(set(nums)):
                return True
            return False
        # If k is shorter than list, slide twice wide window.
        else:
            for a in range(k, length - k):
                b = nums[a - k : a + k + 1]
                b.remove(nums[a])
                if nums[a] in set(b):
                    return True
        return False

    def contains_nearby_duplicate_e(self, nums: list[int], k: int) -> bool:
        """
        Tells us if there exists a particular number twice within a window `k`
        inside of `nums`.

        Args:
            `nums`: The list of numbers to look through.
            `k`: The max distance between any two identical numbers.
        Returns:
            `True/False`: If there is two of a single number within a distance
                `k` from one another inside the list.
        """

        # Remove edge-case.
        if k == 0:
            return False
        # If k is longer than our list, see if set() removes any.
        length = len(nums)
        if k >= length - 1:
            if length != len(set(nums)):
                return True
            return False
        # If k is shorter than list, look for seen values.
        else:
            seen = {}
            for i, value in enumerate(nums):
                if value in seen:
                    if i - seen[value] <= k:
                        return True
                seen[value] = i
        return False

    def contains_nearby_duplicate_f(self, nums: list[int], k: int) -> bool:
        """
        Tells us if there exists a particular number twice within a window `k`
        inside of `nums`.

        Args:
            `nums`: The list of numbers to look through.
            `k`: The max distance between any two identical numbers.
        Returns:
            `True/False`: If there is two of a single number within a distance
                `k` from one another inside the list.
        """

        # Remove edge-case.
        if k == 0:
            return False
        # If k is longer than our list, see if set() removes any.
        length = len(nums)
        if k >= length - 1:
            if length != len(set(nums)):
                return True
            return False
        # If k is shorter than list, look for seen values.
        else:
            seen = {}
            for i, value in enumerate(nums):
                if value in seen and i - seen[value] <= k:
                    return True
                seen[value] = i
        return False
