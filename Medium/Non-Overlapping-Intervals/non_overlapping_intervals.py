"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def erase_overlap_intervals(self, intervals: list[list[int]]) -> int:
        """
        Given a list of intervals that may be overlapping, we're interested in
        removing some intervals such that none are overlapping. What's the
        least number of removals we can do?

        Args:
            `intervals`: A list of intervals.
        Returns:
            `output`: A count of removals.
        """

        def sort_help(interval: list) -> float:
            """
            For sorting with preference to end, with length after.

            Args:
                `interval`: Our list to sort
            Returns:
                `output`: A found number.
            """

            begin = interval[0]
            end = interval[1]
            length = end - begin
            output = end
            output += 1 / (length + 1)
            return output

        # Edge-case: Single item
        if len(intervals) == 1:
            return 0

        # Sort by the end values, then start values. We're building a stack of
        # intervals that collide with our furthest left found item. When we
        # find a new interval that is outside of our group, we clear our stack,
        # to then add that item, which is guaranteed as newest left-most.
        intervals.sort(key=sort_help)
        stack = []
        stack.append(intervals[0])
        remove_count = 0
        for i in range(1, len(intervals)):
            current_right = stack[0][1]
            inter = intervals[i]
            if inter[0] < current_right:
                stack.append(inter)
            else:
                while len(stack) > 0:
                    stack.pop()
                    remove_count += 1
                remove_count -= 1
                stack.append(inter)

        # At end, handle last stack.
        while len(stack) > 0:
            stack.pop()
            remove_count += 1
        remove_count -= 1
        return remove_count
