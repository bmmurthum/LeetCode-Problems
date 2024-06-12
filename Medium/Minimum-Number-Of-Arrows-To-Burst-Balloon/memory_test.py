""" Module to report peak-memory used by method """

import tracemalloc


class Solution:
    """Given class by LeetCode to perform methods in"""

    # My solution
    def find_min_arrow_shots_1(self, points: list[list[int]]) -> int:
        """Returns the minimum number of shots to take down a variety of balloons."""
        total_balloons = len(points)
        initial_balloons = total_balloons

        points.sort()

        l_index = 0
        arrows_used = 0
        while total_balloons > 0:
            l_left = points[l_index][0]
            l_right = points[l_index][1]
            i = l_index + 1
            total_balloons -= 1

            while i < initial_balloons:
                cur_left = points[i][0]
                cur_right = points[i][1]
                if cur_left > l_right:
                    l_index += 1
                    break
                if l_left <= cur_right and l_right >= cur_left:
                    l_right = min(cur_right, l_right)
                    l_left = max(cur_left, l_left)
                    total_balloons -= 1
                    l_index += 1
                i += 1
            arrows_used += 1
        return arrows_used

    def find_min_arrow_shots_2(self, points: list[list[int]]) -> int:
        """Someone else's solution"""
        points.sort(key=lambda x: x[1])
        end = points[0][1]
        c = 1
        for i in range(1, len(points)):
            if points[i][0] > end:
                c += 1
                end = points[i][1]
        return c

    def find_min_arrow_shots_3(self, points: list[list[int]]) -> int:
        """Someone else's solution"""
        points = sorted(points, key=lambda x: x[1])
        _count = 0
        _end = None
        for point in points:
            if _end is None or _end < point[0]:
                _end = point[1]
                _count += 1
        return _count


# Testing Memory Allocation
sol = Solution()
x = [
    [2, 3],
    [7, 15],
    [5, 12],
    [4, 5],
    [8, 13],
    [9, 16],
    [5, 8],
    [8, 16],
    [3, 4],
    [8, 17],
]

# find_min_arrow_shots_1()
y = x.copy()
tracemalloc.start()
RESULT = sol.find_min_arrow_shots_1(y)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("find_min_arrow_shots_1(): " + TRACED_MEMORY_PEAK + " blocks")


# find_min_arrow_shots_2()
y = x.copy()
tracemalloc.start()
RESULT = sol.find_min_arrow_shots_2(y)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("find_min_arrow_shots_2(): " + TRACED_MEMORY_PEAK + " blocks")


# find_min_arrow_shots_3()
y = x.copy()
tracemalloc.start()
RESULT = sol.find_min_arrow_shots_3(y)
TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("find_min_arrow_shots_3(): " + TRACED_MEMORY_PEAK + " blocks")
