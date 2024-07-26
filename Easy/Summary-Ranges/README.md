# Summary Ranges

**Description:**

You are given a sorted unique integer array `nums`.

A range `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

- `"a->b" if a != b`
- `"a" if a == b`

**Constraints:**

- `0 <= nums.length <= 20`
- `-231 <= nums[i] <= 231 - 1`
- All the values of `nums` are unique.
- `nums` is sorted in ascending order.

**Examples:**

```text
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

## Overview

For my solution I split the major functions into two steps, (1) finding the critical range points and (2) translating it to the desired string format.

If I were to write this problem myself, I'd have the output not be a list of strings, but a list of tuples. This solution reveals that.

```python
class Solution:
    """Problem given by LeetCode."""

    def summary_ranges(self, nums: list[int]) -> list[str]:
        """
        Generates a minimal list of ranges that cover the given integers.

        Args:
            `nums`: An ascending, sorted list.
        Returns:
            `range_list`: A list of strings that represent a group of ranges
                that contain the numbers in the list.
        """

        # Handle empty case
        if nums == []:
            return []

        # Build the list
        start = 0
        range_list = []
        for i, value in enumerate(nums[1:], 1):
            if value - nums[i - 1] > 1:
                range_list.append([nums[start], nums[i - 1]])
                start = i
        range_list.append([nums[start], nums[len(nums) - 1]])

        # Translate the list
        for i, r in enumerate(range_list):
            if r[0] == r[1]:
                range_list[i] = str(r[0])
            else:
                range_list[i] = f"{r[0]}->{r[1]}"
        return range_list
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's two example cases.
- A mix of positive and negative values
- An empty list
- A single item
- 20 items, all separated
- 20 items, all touching

```text
** Unit Tests **

Unit Tests Ran: 7
Methods Tested: 3
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 100% code coverage on all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report
Name                  Stmts   Miss  Cover
-----------------------------------------
call_tests.py            13      0   100%
memory_tests.py          84      0   100%
summary_ranges.py        16      0   100%
summary_ranges_2.py      17      0   100%
summary_ranges_3.py      19      0   100%
testcases.py             29      0   100%
time_tests.py            75      0   100%
unit_tests.py           100      0   100%
-----------------------------------------
TOTAL                   353      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 6: 20 items, not touching.
      summary_ranges(): 1695 blocks
    summary_ranges_2(): 1591 blocks
    summary_ranges_3(): 1583 blocks

Testcase 7: 20 items, all together.
      summary_ranges(): 643 blocks
    summary_ranges_2(): 470 blocks
    summary_ranges_3(): 462 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a test case. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 6: 20 items, not touching.
      summary_ranges() runtime: 1.3097e-02 sec
    summary_ranges_2() runtime: 1.0358e-02 sec
    summary_ranges_3() runtime: 7.5488e-03 sec

Testcase 7: 20 items, all together.
      summary_ranges() runtime: 4.1572e-03 sec
    summary_ranges_2() runtime: 4.4699e-03 sec
    summary_ranges_3() runtime: 3.7608e-03 sec
```

## Reflections

My solution is within the herd of performance. If I were to clean it up, it'd be do have my "translate" step be integrated as these other solutions do.

Across each of these solutions, we use a different iteration method, while doing a very similar logic.

## Solution Variations

### summary_ranges_2.py

```python
class Solution:
    def summary_ranges_2(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ranges = []
        n = len(nums)
        i = 0
        while i < n:
            start = nums[i]
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            if j > i:
                ranges.append(f"{start}->{nums[j]}")
            else:
                ranges.append(str(start))
            i = j + 1
        return ranges
```

### summary_ranges_3.py

```python
class Solution:
    def summary_ranges_3(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        result = []
        prev_num = nums[0]
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev_num + 1:
                prev_num = nums[i]
            else:
                if prev_num != start:
                    result.append(f"{start}->{prev_num}")
                else:
                    result.append(f"{start}")
                start = nums[i]
                prev_num = nums[i]
        if prev_num != start:
            result.append(f"{start}->{prev_num}")
        else:
            result.append(f"{start}")
        return result

```
