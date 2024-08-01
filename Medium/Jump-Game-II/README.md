# Jump Game II

**Description:**

You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

- `0 <= j <= nums[i]`
- `i + j < n`

Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

**Constraints:**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

**Examples:**

```text
Input: nums = [2,3,1,1,4]
Output: 2

Input: nums = [2,3,0,1,4]
Output: 2
```

## Overview

My solution iterates through the `nums` list keeping a list `jump_count` of how many jumps it'd take to get to any given position, which becomes an input for a new calculation as we get further in. This eventually reaches the end.

```python
class Solution:
    """Problem given by LeetCode."""

    def jump(self, nums: list[int]) -> int:
        """
        Returns the minimum number of "jumps" to get from the first index to
        the last if each value represents how far you can jump from the current
        value.

        Given lists are confirmed to have possibility of reaching the end.

        Args:
            `nums`: A list of distances jumpable.
        Return:
            `new_count`: The minimum number of jumps to reach the end.
        """

        # Handle single item case.
        if len(nums) == 1:
            return 0

        # A list of how many jumps to get to a position.
        jump_count = [None] * len(nums)
        jump_count[0] = 0

        # At any position declare the furthest points it can reach as reachable
        # in "current count" plus one jumps. If that is less than a number
        # previously recorded, overwrite.

        # If the ending range of a jump is the last index, we can stop search.
        for i in range(len(nums)):
            new_count = jump_count[i] + 1
            end_range = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, end_range + 1):
                if jump_count[j] is None or new_count < jump_count[j]:
                    jump_count[j] = new_count
            if end_range == len(nums) - 1:
                return new_count
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's two example cases.
- Many ones with zero as last value.
- All ones
- Jumping a gap
- All tens, options for less optimal paths
- Larger cases

```text
** Unit Tests **

Unit Tests Ran: 8
Methods Tested: 3
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 100% code coverage of all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report
Name                Stmts   Miss  Cover
---------------------------------------
call_tests.py          13      0   100%
jump_game_ii.py        14      0   100%
jump_game_ii_2.py      12      0   100%
jump_game_ii_3.py      11      0   100%
memory_tests.py        84      0   100%
testcases.py           37      0   100%
time_tests.py          75      0   100%
unit_tests.py         108      0   100%
---------------------------------------
TOTAL                 354      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 7: 1000 ones.
      jump(): 32544 blocks
    jump_2(): 736 blocks
    jump_3(): 740 blocks

Testcase 8: 1000 ones. Jumpable.
      jump(): 8712 blocks
    jump_2(): 600 blocks
    jump_3(): 648 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 6: 1000 Ones.
      jump() runtime: 7.7200e-05 sec
    jump_2() runtime: 9.8200e-05 sec
    jump_3() runtime: 8.9600e-05 sec

Testcase 7: 1000 ones. Jumpable.
      jump() runtime: 1.7086e-01 sec
    jump_2() runtime: 1.3922e-01 sec
    jump_3() runtime: 1.4655e+01 sec
```

## Reflections

In a dynamic programming fashion, this method uses more memory to store results of previous calculations in order to aid further calculations. This solution reveals itself with my Testcase 7 of a longer list of 1s, using more memory but ending up faster than the other solutions.

## Solution Variations

### jump_game_ii_2.py

```python
class Solution:
    def jump_2(self, nums: list[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(nums) - 1:
            farthest = 0
            for x in range(l, r + 1):
                farthest = max(farthest, x + nums[x])
            l = r + 1
            r = farthest
            res += 1
        return res
```

### jump_game_ii_3.py

```python
class Solution:
    def jump_3(self, nums: list[int]) -> int:
        count = 0
        current = len(nums) - 1
        while current != 0:
            for i, n in enumerate(nums):
                if i + n >= current:
                    count += 1
                    current = i
                    break
        return count
```
