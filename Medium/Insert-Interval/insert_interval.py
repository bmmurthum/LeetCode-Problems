""" Module to find a group of ranges that cover all the integers in a list. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        """
        Given a list of non-overlapping intervals, this method inserts a new
        interval into that list and handles merging now-overlapping intervals.
        We handle this in-place.

        Args:
            `intervals`: A current list of intervals
            `new_interval`: A new interval to insert and merge into `intervals`.
        Returns:
            `intervals`: A new list that represents the changes.
        """

        # If the new interval should be at the beginning, don't do any
        # iterations.
        if len(intervals) > 0 and new_interval[1] < intervals[0][0]:
            intervals.insert(0, new_interval)
            return intervals

        # Look for a starting interval
        start_index = -1
        start_value = -1
        remove_count = 0
        for i, item_a in enumerate(intervals):
            # If we find a good starting interval
            if (
                (new_interval[0] <= item_a[0] and new_interval[1] >= item_a[0])
                or (new_interval[0] <= item_a[1] and new_interval[1] >= item_a[1])
                or (new_interval[0] >= item_a[0] and new_interval[0] <= item_a[1])
                or (new_interval[1] >= item_a[0] and new_interval[1] <= item_a[1])
            ):
                start_index = i
                start_value = min(item_a[0], new_interval[0])
                end_value = max(item_a[1], new_interval[1])
                remove_count = 1
                # Look for an ending interval
                for _, item_b in enumerate(intervals[i + 1 :], i + 1):
                    if new_interval[1] >= item_b[0]:
                        if new_interval[1] <= item_b[1]:
                            # Remove some amount of items from intervals
                            # Insert the new interval at this position
                            # Return
                            interval_insert = [start_value, item_b[1]]
                            for _ in range(remove_count + 1):
                                intervals.pop(start_index)
                            intervals.insert(start_index, interval_insert)
                            return intervals
                        else:
                            remove_count += 1
                    # There was only one item to replace
                    else:
                        for _ in range(remove_count):
                            intervals.pop(start_index)
                        intervals.insert(start_index, [start_value, end_value])
                        return intervals
                break
            # If we've passed the possibility of finding a starting interval
            if new_interval[1] < item_a[0]:
                intervals.insert(i, new_interval)
                return intervals
        # Never found a start position for our new interval
        # Also handles case of no items inside intervals list
        if start_index == -1:
            intervals.append(new_interval)
            return intervals
        # Found a start position, but no ending.
        else:
            end_value = max(intervals[-1][1], new_interval[1])
            for _ in range(remove_count):
                intervals.pop(start_index)
            intervals.insert(start_index, [start_value, end_value])
            return intervals
