""" Module to report peak-memory used by method """

import tracemalloc


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
        """Merges separated intervals."""
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


# Testing Memory Allocation
sol = Solution()
x = [
    [1, 2],
    [2, 3],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 14],
    [10, 11],
    [11, 12],
    [15, 16],
    [17, 18],
    [22, 26],
]

# merge_1()
y = x.copy()
tracemalloc.start()
RESULT = sol.merge_1(y)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("merge_1(): " + TRACED_MEMORY_PEAK + " blocks")

# merge_2()
y = x.copy()
tracemalloc.start()
RESULT = sol.merge_2(y)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("merge_2(): " + TRACED_MEMORY_PEAK + " blocks")
