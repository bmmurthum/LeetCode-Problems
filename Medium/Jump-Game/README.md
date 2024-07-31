# Jump Game

**Description:**

You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

**Constraints:**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

**Examples:**

```text
Input: nums = [2,3,1,1,4]
Output: true

Input: nums = [3,2,1,0,4]
Output: false
```

## Overview

For my solution I keep a parallel list of booleans on if a given index is reachable `can_reach`. We update this as we iterate through the `nums` list. This is meant to perform as a basic dynamic-programming design.

If we ever cross an index in which `can_reach[i] is False` we know that we cannot reach and the end and can stop iterating early.

If at any point the last index of `can_reach` is `True` we can stop early knowing that the end is reachable.

```python
class Solution:
    """Problem given by LeetCode."""

    def can_jump(self, nums: list[int]) -> bool:
        """
        Looking at a list of values that represent how far further in the list
        you could jump to, is there a path to the last value?

        Args:
            `nums`: A list of how-far-can-jump values.
        Returns:
            `True/False`: Whether the last index can be reached.
        """

        # Create list of noting if an index is reachable.
        can_reach = [False] * len(nums)
        can_reach[0] = True

        # Look for reach
        for i in range(len(nums) - 1):
            if can_reach[i] is False:
                # This current value isn't reachable
                return False
            elif nums[i] != 0:
                if i + nums[i] >= len(nums) - 1:
                    # This value reaches last index
                    return True
                for j in range(i + 1, i + nums[i] + 1):
                    can_reach[j] = True
        return can_reach[-1]
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's three example cases
- All descending numbers
- All ascending numbers

```text
** Unit Tests **

Unit Tests Ran: 9
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
Name              Stmts   Miss  Cover
-------------------------------------
call_tests.py        13      0   100%
jump_game.py         13      0   100%
jump_game_2.py        7      0   100%
jump_game_3.py       10      0   100%
memory_tests.py      84      0   100%
testcases.py         37      0   100%
time_tests.py        75      0   100%
unit_tests.py       116      0   100%
-------------------------------------
TOTAL               355      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 6: Jump several zeroes to end.
      can_jump(): 752 blocks
    can_jump_2(): 528 blocks
    can_jump_3(): 480 blocks

Testcase 3: Many ones. Zero as last number.
      can_jump(): 728 blocks
    can_jump_2(): 520 blocks
    can_jump_3(): 472 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 6: Jump several zeroes to end.
      can_jump() runtime: 3.5325e-03 sec
    can_jump_2() runtime: 1.4398e-03 sec
    can_jump_3() runtime: 2.2609e-03 sec

Testcase 3: Many ones. Zero as last number.
      can_jump() runtime: 5.0962e-03 sec
    can_jump_2() runtime: 1.4459e-03 sec
    can_jump_3() runtime: 1.7921e-03 sec
```

## Reflections

This problem was marked with a tag of "dynamic programming," so I implemented a quick idea of keeping track of if the current index is reachable, with a use of more memory. This with a vision of a recursive solution within possibility.

I'm not sure this problem really calls for recursion or dynamic programming with how simple it is.

## Solution Variations

### jump_game_2.py

Starting at the last index, "does anyone reach this?" Then ask if anyone reaches that index that reaches the one before it.

```python
class Solution:
    def can_jump_2(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0
```

### jump_game_3.py

`farthest` is a pointer to the farthest index reachable, if we ever reach it, we know we can't reach the end.

```python
class Solution:
    def can_jump_3(self, nums: list[int]) -> bool:
        farthest = 0
        for num in nums:
            if farthest < 0:
                return False
            elif farthest < num:
                farthest = num
            farthest -= 1
        return True
```
