# Merge Intervals

**Description:**

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Example:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
```

## Overview

To merge our connected intervals, we do the following:

1. Create an empty list `new_list` to append to later.
2. Sort the given `intervals` list so that we can traverse it while knowing that each item's lowest value is equal to or greater than the last.
3. Set up an initial `left` and `right` window that takes the values of the first given item in the `intervals` list. 
4. Within a loop, starting at the second item, we look at the current interval's lowest value `w_left` and if:
   - it's valid to be merged, we increase the window to the higher value between current item's right `w_right` and the window's `right`.
   - if not to be merged, we append the saved window to our `new_list` and then create a new window to be considered and iterate to the next item.
5. After the loop, the window is left hanging, so we append the window.
6. Then return the `new_list`.

```python
# My solution
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
```

## Tests

**Unit Testing**

We implemented unit-tests for this problem with `import unittest`. We checked for:
- Simple case
- Overlap on edges
- One interval encapsulating another
- Single item
- Larger list of intervals

**Code Coverage**

We received 100% code coverage on each tested method from the unit-test using the `coverage.py` tool.

```
> coverage run unit_test.py
> coverage report -m 
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
merge_intervals.py      27      0   100%
unit_test.py            49      0   100%
--------------------------------------------------
TOTAL                   76      0   100%
```

**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of two similar functions on a 10 item case. We compare my solutions, seen below.

Memory blocks used:

- `merge_1()`: 672 blocks
- `merge_2()`: 616 blocks

**Process Time Testing**

I used `timeit` to isolate the individual functions on the same input.

My solution `merge_1()`, with `sort()` is 21% faster than the solution `merge_2()` with an included lambda `sort(key=lambda x: x[0])`.

- `merge_1()`: 1.041 x 10^-6 sec
- `merge_2()`: 1.326 x 10^-6 sec


## Reflections

We looked through other solutions to see if there was a speedier variation. This seems to be the common answer. Other people used lambda in their sorts, so I did a speed test for that.

## Solution Variations

```python
# My solution, with lambda in sort()
def merge_2(self, intervals: list[list[int]]) -> list[list[int]]:
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
```