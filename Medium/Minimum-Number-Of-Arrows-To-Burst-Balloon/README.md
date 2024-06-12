# Minimum Number of Arrows to Burst Balloon

**Description:**

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon whose horizontal diameter stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is burst by an arrow shot at x if `xstart <= x <= xend`. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

**Example:**

```
Input: points = [[1,2],[2,3],[4,5]]
Output: 2
Explanation: Two arrows, at "2" and "4"

      BBB
  BBB
BBB
1-2-3-4-5

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
```

## Overview

My solution iterates over the given list of balloons `points` and considers which other balloons may fit within a shrinking interval `[l_left,l_right]` that shoots more than one balloon. My solution grew from the idea that: with a set of balloons, the left-most balloon **must** be shot eventually, what other ones can come with it?

First we sort `points` by its left-most point and initialize some counter variables.

In loop, while there are balloons left `total_balloons > 0`, we look at our left-most balloon (at index of `l_index`) and find which "current" balloons (at index `i`) after it have overlapping positions `l_left <= cur_right and l_right >= cur_left`. If true, we shrink the range of consideration to be within the area shared by both balloons and then consider the next "current" balloon. When we find a balloon that does not share any overlap `cur_left > l_right` we stop looking in this series, and then consider a new left-most balloon at `l_index`.

```python
# My solution
def find_min_arrow_shots_1(self, points: list[list[int]]) -> int:
    total_balloons = len(points)
    initial_balloons = total_balloons
    points.sort()
    arrows_used = 0

    l_index = 0 # Left-most balloon index
    
    # Considering our current left-most balloon, what others can also be shot?
    while total_balloons > 0:
        l_left = points[l_index][0]
        l_right = points[l_index][1]
        i = l_index + 1 # Index of the next-also-considered
        total_balloons -= 1 # Pop our left-most balloon
        # What balloons after left-most can be shot simultaneously?
        while i < initial_balloons:
            cur_left = points[i][0]  # Current balloon
            cur_right = points[i][1] # Current balloon
            if cur_left > l_right:
                l_index += 1
                break
            if l_left <= cur_right and l_right >= cur_left:
                l_right = min(cur_right, l_right)
                l_left = max(cur_left, l_left)
                total_balloons -= 1 # Pop our current balloon
                l_index += 1
            i += 1
        arrows_used += 1
    return arrows_used
```

## Tests

**Unit Testing**

We implemented unit-tests for this problem with `import unittest`. We checked for:
- Simple case
- No overlapping balloons
- Competing overlap, in which the order of consideration affects outcome
- Single balloon
- All balloons shot in one arrow
- All balloons in same position
- A more complicated shrinking case
- Balloons with negative positions

Our test checks the validity of each included similar method.

**Code Coverage**

We received 100% code coverage on each tested method from the unit-test using the `coverage.py` tool.

```
> coverage run unit_test.py
> coverage report -m 
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
minimum_number_of_arrows_to_burst_balloon.py      44      0   100%
unit_test.py                                      85      0   100%
----------------------------------------------------------------------------
TOTAL                                            129      0   100%
```

**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of the functions on a variety 10-balloon case. We compare my solution with two other solutions, seen below.

Memory blocks used:

- `find_min_arrow_shots_1()`: 48 blocks
- `find_min_arrow_shots_2()`: 152 blocks
- `find_min_arrow_shots_3()`: 304 blocks

**Process Time Testing**

I used `timeit` to isolate the individual functions on the same input.

My solution `find_min_arrow_shots_1()` is 2.5x slower than the fastest solution `find_min_arrow_shots_2()` with a variety 10-balloon case.

- `find_min_arrow_shots_1()`: 1.644 x 10^-6 sec
- `find_min_arrow_shots_2()`: 0.663 x 10^-6 sec
- `find_min_arrow_shots_3()`: 0.688 x 10^-6 sec


## Reflections

For some period I was trying to work a solution with the balloon `points` sorted by their width, to start looking for best solutions starting with largest balloons. That proved to be an issue, and was scrapped.

When I looked at a given set up and saw that there **must** be one arrow dedicated to edge balloons, I considered alternating left and right edges for a moment, until I saw that removing a left-most group results in an identical situation.

The speed of the other's solutions comes from their not-shrinking-interval manipulation and their use of index to consider conclusion. The question was proposed in a shrinking-interval collection of questions and that pushed me in that direction.

I also considered removing balloons from the list on "being shot" `del point[i]`, but this proved to be slow on account of removing from large lists forces Python to do reassignment of each index. It was better to leave the given list as is, no need for editting of `points`.

## Solution Variations

`find_min_arrow_shots_2()` does similar logic, but without many of the helper variables, and no shrinking-window setup. If the right-edge of the left-most balloon `end` does not overlap with the currently looked at balloon, consider an arrow shot `c` and update `end` to be the right-edge of this new index `i`.

It uses the index to be the counter of how many balloons have been considered. I like that.

I considered using a lamda in the sort, `points.sort(key=lambda x: x[1])`. For my logic, I was sorting by the first value, so I saw that `points.sort()` did the same thing and figured there may be a speed increase without an internal function and assignment.

`152 memory blocks` & `0.663 x 10^-6 sec`
```python
# Someone else's solution
def find_min_arrow_shots_2(self, points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    end = points[0][1]
    c = 1
    for i in range(1, len(points)):
        if points[i][0] > end:
            c += 1
            end = points[i][1]
    return c
```

`find_min_arrow_shots_3()` sorts by the right-edge of balloons, to then do similar logic.

The use of `sorted()` creates a new list instead of the in-place option of `sort()`. I opted for `sort()` for less memory use and time in assignment, though it will change the given list of balloons, if that initial list order was important outside of our method.

The `for point in points:` adds some readability instead of including the index of the current-looked-at balloon. I like that.

`304 memory blocks` & `0.688 x 10^-6 sec`
```python
# Someone else's solution
def find_min_arrow_shots_3(self, points: list[list[int]]) -> int:
    points = sorted(points, key=lambda x: x[1])
    _count = 0
    _end = None
    for point in points:
        if _end is None or _end < point[0]:
            _end = point[1]
            _count += 1
    return _count
```