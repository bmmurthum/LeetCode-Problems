"""Module for testing function time performance"""

import timeit

NUM_TESTS = 500


# Generate a test-case
width = 10
height = 10
matrix = []
for x in range(0, width):
    matrix.append([])
    for y in range(0, height):
        matrix[x].append(x + y)


# My solution
MYSETUP = """
class Solution:
    def spiral_order_1(self, matrix: list[list[int]]) -> list[int]:
        height = len(matrix)
        width = len(matrix[0])
        output_list = []
        start_x = 0
        start_y = 0
        while True:
            end_right = width - 1
            for a in range(start_x, start_x + end_right + 1):
                output_list.append(matrix[start_y][a])
            if height < 2:
                break
            end_down = height - 1
            for a in range(start_y + 1, start_y + end_down + 1):
                output_list.append(matrix[a][start_x + end_right])
            if width < 2:
                break
            end_left = width
            for a in range(1, end_left):
                output_list.append(matrix[start_y + end_down][start_x + end_right - a])
            end_up = height - 1
            for a in range(1, end_up):
                output_list.append(
                    matrix[start_y + end_down - a][start_x + end_left - width]
                )
            width -= 2
            height -= 2
            start_x += 1
            start_y += 1
            if width < 1:
                break
        return output_list
"""
MYCODE = (
    """
sol = Solution()
matrix = """
    + str(matrix)
    + """
RESULT = sol.spiral_order_1(matrix)
"""
)
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("spiral_order_1():" + TIME_PER_RUN)


# Someone else's solution
MYSETUP = """
class Solution:
    def spiral_order_2(self, matrix: list[list[int]]) -> list[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r, t, b = 0, COLS, 0, ROWS
        res = []
        while l < r and t < b:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                res.append(matrix[i][r - 1])  # right is OOB
            r -= 1
            if not (l < r and t < b):  # pointer crossed, exit early
                break
            for i in range(r - 1, l - 1, -1):  # left is not inclusive
                res.append(matrix[b - 1][i])  # bottom is OOB
            b -= 1
            for i in range(b - 1, t - 1, -1):  # top is non inclusive
                res.append(matrix[i][l])
            l += 1
        return res
"""
MYCODE = (
    """
sol = Solution()
matrix = """
    + str(matrix)
    + """
RESULT = sol.spiral_order_2(matrix)
"""
)
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("spiral_order_2():" + TIME_PER_RUN)


# My solution
MYSETUP = """
import numpy as np
class Solution:
    def spiral_order_3(self, matrix: list[list[int]]) -> list[int]:
        n_arr = np.array(matrix)
        output_list = []
        height = n_arr.shape[0]
        width = n_arr.shape[1]
        start_x = 0
        start_y = 0
        while True:
            for a in range(start_x, start_x + width):
                output_list.append(n_arr[start_y][a])
            if height < 2:
                break
            for a in range(start_y + 1, start_y + height):
                output_list.append(n_arr[a][start_x + width - 1])
            if width < 2:
                break
            for a in range(1, width):
                output_list.append(n_arr[start_y + height - 1][start_x + width - 1 - a])
            for a in range(1, height - 1):
                output_list.append(n_arr[start_y + height - 1 - a][start_x])
            width -= 2
            height -= 2
            start_x += 1
            start_y += 1
            if width < 1:
                break
        return output_list
"""
MYCODE = (
    """
sol = Solution()
matrix = """
    + str(matrix)
    + """
RESULT = sol.spiral_order_3(matrix)
"""
)
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("spiral_order_3():" + TIME_PER_RUN)
