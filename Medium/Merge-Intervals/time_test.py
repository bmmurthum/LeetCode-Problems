"""Module for testing function time performance"""

import timeit

NUM_TESTS = 500


# My solution
MYSETUP = """
class Solution:
    def merge_1(self, intervals: list[list[int]]) -> list[list[int]]:
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
"""
MYCODE = """
RESULT = sol.merge_1(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("merge_1():" + TIME_PER_RUN)


# Someone else's solution
MYCODE = """
RESULT = sol.merge_2(x)
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("merge_2():" + TIME_PER_RUN)
