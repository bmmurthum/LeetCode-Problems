""" Module to report peak-memory used by method """

import tracemalloc
import numpy as np


class Solution:
    """Given class by LeetCode to perform methods in"""

    # My solution
    def spiral_order_1(self, matrix: list[list[int]]) -> list[int]:
        """
        Returns a `list` of elements of the path of traversing the matrix in a spiral pattern.
        """
        height = len(matrix)
        width = len(matrix[0])
        output_list = []
        start_x = 0
        start_y = 0
        while True:
            # Go right
            end_right = width - 1
            for a in range(start_x, start_x + end_right + 1):
                output_list.append(matrix[start_y][a])
            if height < 2:
                break
            # Go down
            end_down = height - 1
            for a in range(start_y + 1, start_y + end_down + 1):
                output_list.append(matrix[a][start_x + end_right])
            if width < 2:
                break
            # Go left
            end_left = width
            for a in range(1, end_left):
                output_list.append(matrix[start_y + end_down][start_x + end_right - a])
            # Go up
            end_up = height - 1
            for a in range(1, end_up):
                output_list.append(
                    matrix[start_y + end_down - a][start_x + end_left - width]
                )
            # Setup for next inner spiral
            width -= 2
            height -= 2
            start_x += 1
            start_y += 1
            if width < 1:
                break
        return output_list

    # Someone else's solution
    def spiral_order_2(self, matrix: list[list[int]]) -> list[int]:
        """
        Returns a `list` of elements of the path of traversing the matrix in a spiral pattern.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r, t, b = 0, COLS, 0, ROWS
        res = []

        while l < r and t < b:
            # get all from top row
            for i in range(l, r):
                res.append(matrix[t][i])
            # once traverse top row, top is shrunk
            t += 1
            # get all right row
            for i in range(t, b):
                res.append(matrix[i][r - 1])  # right is OOB
            # right is shrunk
            r -= 1

            if not (l < r and t < b):  # pointer crossed, exit early
                break

            # get all bottom row
            for i in range(r - 1, l - 1, -1):  # left is not inclusive
                res.append(matrix[b - 1][i])  # bottom is OOB
            # bottom is shrunk
            b -= 1
            # get all left row
            for i in range(b - 1, t - 1, -1):  # top is non inclusive
                res.append(matrix[i][l])
            # left is shrunk
            l += 1
        return res

    # My solution
    def spiral_order_3(self, matrix: list[list[int]]) -> list[int]:
        """
        Returns a `list` of elements of the path of traversing the matrix in a spiral pattern.
        """
        n_arr = np.array(matrix)
        output_list = []
        height = n_arr.shape[0]
        width = n_arr.shape[1]

        start_x = 0
        start_y = 0
        while True:
            # Go right
            for a in range(start_x, start_x + width):
                output_list.append(n_arr[start_y][a])
            if height < 2:
                break
            # Go down
            for a in range(start_y + 1, start_y + height):
                output_list.append(n_arr[a][start_x + width - 1])
            if width < 2:
                break
            # Go left
            for a in range(1, width):
                output_list.append(n_arr[start_y + height - 1][start_x + width - 1 - a])
            # Go up
            for a in range(1, height - 1):
                output_list.append(n_arr[start_y + height - 1 - a][start_x])
            # Setup for next inner spiral
            width -= 2
            height -= 2
            start_x += 1
            start_y += 1
            if width < 1:
                break
        return output_list


# Testing Memory Allocation
# spiral_order_1()
sol = Solution()
m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
tracemalloc.start()
RESULT = sol.spiral_order_1(m)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("spiral_order_1(): " + TRACED_MEMORY_PEAK + " blocks")


# spiral_order_2()
sol = Solution()
m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
tracemalloc.start()
RESULT = sol.spiral_order_2(m)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("spiral_order_2(): " + TRACED_MEMORY_PEAK + " blocks")


# spiral_order_3()
sol = Solution()
m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
tracemalloc.start()
RESULT = sol.spiral_order_3(m)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("spiral_order_3(): " + TRACED_MEMORY_PEAK + " blocks")
