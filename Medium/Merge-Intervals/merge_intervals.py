""" This module holds a function to merge separated intervals if they overlap """


class Solution:
    """Given class by LeetCode to perform methods in"""

    def merge_1(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Merges separated intervals.

        Args:
            `intervals[[int,int]]` - a list of two-value lists that denote left
            and right positions.

        Returns:
            `new_intervals[[int,int]]` - a list of two-value lists as before,
            but with any overlapping intervals merged.
        """
        new_list = []
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        for _, (w_left, w_right) in enumerate(intervals, 1):
            if w_left <= right:
                right = max(w_right, right)
            else:
                new_list.append([left, right])
                left = w_left
                right = w_right
        new_list.append([left, right])
        return new_list

    def merge_2(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Merges separated intervals.

        Args:
            `intervals[[int,int]]` - a list of two-value lists that denote left
            and right positions.

        Returns:
            `new_intervals[[int,int]]` - a list of two-value lists as before,
            but with any overlapping intervals merged.
        """
        new_list = []
        intervals.sort(key=lambda x: x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        for _, (w_left, w_right) in enumerate(intervals, 1):
            if w_left <= right:
                right = max(w_right, right)
            else:
                new_list.append([left, right])
                left = w_left
                right = w_right
        new_list.append([left, right])
        return new_list
