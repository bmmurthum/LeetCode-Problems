# Insert Interval

**Description:**

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

Note that you don't need to modify `intervals` in-place. You can make a new array and return it.

**Constraints:**

- `0 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 105`
- `intervals` is sorted by `starti` in ascending order.
- `newInterval.length == 2`
- `0 <= start <= end <= 105`

**Examples:**

```text
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

## Overview

At first I had a simpler design in mind for this solution, but decided against it on a consideration that this may be faster, in exiting the process as soon as possible.

I intentionally designed with changing `intervals` in-place for the idea of using less memory and faster process in less list creation. This may have limited my ability to write with readability in mind.

At a high-level, this process looks for a first interval in `intervals` that collides with `new_interval` and then looks for an ending interval that collides with `new_interval`. It returns differently in different sorts of cases that can exist.

```python
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
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's two example cases.
- Intervals that are one-value wide.
- One item in `intervals`
- No items in `intervals`
- Many items, becoming one with wide `new_interval`
- New interval in beginning, no collision
- New interval at end, no collision
- New interval completely inside a single interval
  - With other intervals in list
- Original interval completely inside a new interval
  - With multiple initial intervals
- New interval never overlaps, placed in middle of list
- New interval overlaps some intervals in beginning
- New interval overlaps some intervals at end

```text
** Unit Tests **

Unit Tests Ran: 17
Methods Tested: 3
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 100% code coverage on all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report -m
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
call_tests.py             13      0   100%
insert_interval.py        39      0   100%
insert_interval_2.py      15      0   100%
insert_interval_3.py      26      5    81%   18-19, 26, 28-29
memory_tests.py           86      0   100%
testcases.py              86      0   100%
time_tests.py             75      0   100%
unit_tests.py            197      0   100%
----------------------------------------------------
TOTAL                    537      5    99%
```

`insert_interval_3.py` has three separate chunks of conditions that never get called in my unit tests. With their solution being a binary-search on the list, at a glance, these could be related to not having a large enough list `intervals` in a test case.

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 7: Many items now one.
      insert(): 304 blocks
    insert_2(): 192 blocks
    insert_3(): 112 blocks

Testcase 15: New interval never overlaps, within group.
      insert(): 416 blocks
    insert_2(): 192 blocks
    insert_3(): 176 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 7: Many items now one.
      insert() runtime: 3.1750e-04 sec
    insert_2() runtime: 1.8260e-04 sec
    insert_3() runtime: 1.8180e-04 sec

Testcase 15: New interval never overlaps, within group.
      insert() runtime: 3.2870e-04 sec
    insert_2() runtime: 1.8240e-04 sec
    insert_3() runtime: 1.8260e-04 sec
```

## Reflections

My solution ended up being more complex than I initially planned. I didn't account for some unique cases in my testing and LeetCode caught some wrong return values on tests that I didn't write. I'll have to be sure to write all sorts of cases next time.

I initially imagined a simpler design, but decided on this general idea on the basis that we can return from the iterations as soon as possible. The variety of unique cases demands that I account for them, which added more complexity.

## Solution Variations

If this isn't just the cleanest thing to look at.

I'd suggest they don't create a whole new list `result`, but their solution is faster than mine.

### insert_interval_2.py

```python
class Solution:
    def insert_2(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        result = []
        pos = 0
        while pos < len(intervals):
            if intervals[pos][0] > newInterval[1]:
                break
            elif intervals[pos][1] < newInterval[0]:
                result.append(intervals[pos])
            else:
                newInterval = [
                    min(newInterval[0], intervals[pos][0]),
                    max(newInterval[1], intervals[pos][1]),
                ]
            pos += 1
        result.append(newInterval)
        for i in range(pos, len(intervals)):
            result.append(intervals[i])
        return result
```

### insert_interval_3.py

This person does a variety of binary search on the `intervals` list to find where the `newInterval` would be placed. Clever for optimization, though kind of hard to look at. I'd like some comments.

```python
class Solution:
    def insert_3(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        n = len(intervals)
        i = 0
        j = n
        while i < j:
            mid = i + (j - i) // 2
            if intervals[mid][0] <= newInterval[0]:
                i = mid + 1
            else:
                j = mid
        if i != 0 and intervals[i - 1][1] >= newInterval[0]:
            ans = intervals[: i - 1]
            ans.append([intervals[i - 1][0], max(intervals[i - 1][1], newInterval[1])])
        else:
            ans = intervals[:i]
            ans.append(newInterval)
        j = n
        while i < j:
            mid = i + (j - i) // 2
            if intervals[mid][1] >= ans[-1][1]:
                j = mid
            else:
                i = mid + 1
        if i != n and intervals[i][0] <= ans[-1][1]:
            ans[-1][1] = max(intervals[i][1], ans[-1][1])
            ans += intervals[i + 1 :]
        else:
            ans += intervals[i:]
        return ans
```

This person also excluded their `class Solution:` in LeetCode's submission area and added this to the end of their solution. I imagine it allows for their solution to be recorded with a faster finish time.

```python
# if __name__ == "__main__":
#     import json, sys

#     with open("user.out", "w") as f:
#         data = map(json.loads, sys.stdin)
#         testcases = zip(*[iter(data)] * 2, strict=True)
#         for intervals, interval in testcases:
#             result = insert(intervals, interval)
#             print(json.dumps(result, separators=(",", ":")), file=f)
#     sys.exit()
```
