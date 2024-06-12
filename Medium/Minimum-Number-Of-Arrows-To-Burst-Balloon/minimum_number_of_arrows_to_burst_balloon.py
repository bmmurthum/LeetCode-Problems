""" This module contains a method for calculating the minimum shots to hit overlapping balloons. """


class Solution:
    """Given class by LeetCode to perform methods in"""

    def find_min_arrow_shots_1(self, points: list[list[int]]) -> int:
        """Returns the minimum number of shots to take down a variety of balloons."""
        total_balloons = len(points)
        initial_balloons = total_balloons
        points.sort()
        arrows_used = 0

        l_index = 0  # Index of current left-most balloon

        # Considering our current left-most balloon, what others can also be shot?
        while total_balloons > 0:
            l_left = points[l_index][0]
            l_right = points[l_index][1]
            i = l_index + 1  # Index of the next-also-considered
            total_balloons -= 1  # Pop our left-most balloon

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
