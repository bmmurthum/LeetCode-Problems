# Contains Duplicate II

**Description:**

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 105`

**Examples:**

```text
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Overview

For this solution, first we handle the unique cases of (1) a `k` value of `0`, which would never be `True` and (2) if `k` is equal/longer than the `nums` list, which allows us to simply check on if `nums` is shorter when converted to a set.

After this, our process is to build a dictionary/set of values that we have seen and their index as we iterate through `nums`. If we have seen a value before, we look to see if its near enough. On successful find, we return `True`. If finishing iteration without success, this returns `False`.

```python
class Solution:
    """Problem given by LeetCode."""
    def contains_nearby_duplicate_f(self, nums: list[int], k: int) -> bool:
            """
            Tells us if there exists a particular number twice within a window `k`
            inside of `nums`.

            Args:
                `nums`: The list of numbers to look through.
                `k`: The max distance between any two identical numbers.
            Returns:
                `True/False`: If there is two of a single number within a distance
                    `k` from one another inside the list.
            """

            # Remove edge-case.
            if k == 0:
                return False
            # If k is longer than our list, see if set() removes any.
            length = len(nums)
            if k >= length - 1:
                if length != len(set(nums)):
                    return True
                return False
            # If k is shorter than list, look for seen values.
            else:
                seen = {}
                for i, value in enumerate(nums):
                    if value in seen and i - seen[value] <= k:
                        return True
                    seen[value] = i
            return False
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We ran this for my 6 varied solutions.

We checked for:

- LeetCode's three example cases.
- `K` larger than the list.
- `K` size equals 0.
- `K` size matches list size.
- List all the same number
- Mix of positive and negative values.
- 2000-long list with success find. `K` equals 10.
- 2000-long list with no matches. `K` equals 10.
- 2000-long list with no matches. `K` longer than list.

```text
** Unit Tests **

Unit Tests Ran: 11
Methods Tested: 6
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 100% code coverage on the methods with each test suite using the `coverage.py` tool.

Missing coverage in `memory_test.py` and `time_test.py` are in string formatting for display.

```PowerShell
> coverage run call_tests.py
> coverage report
Name                       Stmts   Miss  Cover
----------------------------------------------
call_tests.py                 13      0   100%
contains_duplicate_II.py      80      0   100%
memory_tests.py              132      2    98%
testcases.py                  56      0   100%
time_tests.py                171      3    98%
unit_tests.py                150      0   100%
----------------------------------------------
TOTAL                        602      5    99%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solutions against the others' solutions.

`contains_nearby_duplicate_b()` uses much 100x less memory than the fastest case, while being 3x slower.

```text
** Memory Tests **

Testcase 9: 2000-long case.
    contains_nearby_duplicate_a(): 1276 blocks
    contains_nearby_duplicate_b(): 1260 blocks
    contains_nearby_duplicate_c(): 164452 blocks
    contains_nearby_duplicate_d(): 3388 blocks
    contains_nearby_duplicate_e(): 142144 blocks
    contains_nearby_duplicate_f(): 142144 blocks

Testcase 11: 2000-long case. No matches. K longer than list.
    contains_nearby_duplicate_a(): 164452 blocks
    contains_nearby_duplicate_b(): 164444 blocks
    contains_nearby_duplicate_c(): 164452 blocks
    contains_nearby_duplicate_d(): 164436 blocks
    contains_nearby_duplicate_e(): 164444 blocks
    contains_nearby_duplicate_f(): 164444 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a test case. The recorded time represents an average time to find the result once.

`contains_nearby_duplicate_e()` is the fastest.

```text
** Time Tests **

Testcase 9: 2000-long case.
    contains_nearby_duplicate_a() runtime: 7.4368e-02 sec
    contains_nearby_duplicate_b() runtime: 6.9315e-02 sec
    contains_nearby_duplicate_c() runtime: 1.7785e+00 sec
    contains_nearby_duplicate_d() runtime: 1.4775e-01 sec
    contains_nearby_duplicate_e() runtime: 2.7697e-02 sec
    contains_nearby_duplicate_f() runtime: 3.0336e-02 sec

Testcase 11: 2000-long case. No matches. K longer than list.
    contains_nearby_duplicate_a() runtime: 1.5826e-03 sec
    contains_nearby_duplicate_b() runtime: 1.3138e-03 sec
    contains_nearby_duplicate_c() runtime: 8.5211e-01 sec
    contains_nearby_duplicate_d() runtime: 1.2351e-03 sec
    contains_nearby_duplicate_e() runtime: 1.2594e-03 sec
    contains_nearby_duplicate_f() runtime: 1.3263e-03 sec

Testcase 5: k == 0.
    contains_nearby_duplicate_a() runtime: 2.6700e-05 sec
    contains_nearby_duplicate_b() runtime: 2.5800e-05 sec
    contains_nearby_duplicate_c() runtime: 2.5900e-05 sec
    contains_nearby_duplicate_d() runtime: 2.5000e-05 sec
    contains_nearby_duplicate_e() runtime: 2.4500e-05 sec
    contains_nearby_duplicate_f() runtime: 2.4200e-05 sec
```

## Reflections

LeetCode didn't accept my first solutions on a time-limit-exceeded warning. This problem supplies us with large lists and suggests manipulations of these lists which can be costly in time and memory. This pushes us to look for clever use of sets, and to use Python's primitives correctly.

In testing, to find a faster solution, I kept running variations against one another on large cases.

## Solution Variations

### contains_nearby_duplicate_a()

This method looks at any window (size `k`) of the overall `nums` list and converts that window to a set to see if the conversion removes any duplicates. I thought this was a good idea, but LeetCode gave us a Time-Limit-Exceeded on this case. The conversion of the window to a set, and then a `len()` call may be too time costly.

```python
# def contains_nearby_duplicate_a(self, nums: list[int], k: int) -> bool:
#         if k == 0:
#             return False
#         length = len(nums)
#         if k >= length - 1 and length != len(set(nums)):
#             return True
#         else:
            for a in range(length - k):
                if len(set(nums[a : a + k + 1])) - 1 != k:
                    return True
#         return False
```

### contains_nearby_duplicate_b()

This looks at each value in the `nums` list to see if there exists a duplicate in the set in front of it. I figured `x in set()` might be an efficient check as `set()` is hashed by Python. I think the conversion of the list to the set is time costly.

```python
# def contains_nearby_duplicate_b(self, nums: list[int], k: int) -> bool:
#         if k == 0:
#             return False
#         length = len(nums)
#         if k >= length - 1 and length != len(set(nums)):
#             return True
#         else:
            for a in range(length - k):
                if nums[a] in set(nums[a + 1 : a + k + 1]):
                    return True
#         return False
```

### contains_nearby_duplicate_c()

For each value in the `nums` list, we looked at all cases of it in the list to see if it had an matching neighbors, then moved to the next value.

This is the slowest of the group. I suspect too many calls and manipulations of the potentially-large list.

```python
# def contains_nearby_duplicate_c(self, nums: list[int], k: int) -> bool:
#         if k == 0:
#             return False
#         length = len(nums)
#         if k >= length - 1 and length != len(set(nums)):
#             return True
#         else:
            for item in set(nums):
                a = nums.index(item)
                while a + k < length:
                    try:
                        if nums[a] in set(nums[a + 1 : a + k + 1]):
                            return True
                        a = nums.index(item, a + 1)
                    except:
                        break
#         return False
```

### contains_nearby_duplicate_d()

In this solution I was exploring if it was any more efficient to have a sliding window that looked forward and backward behind the value that I was interesting in. It would potentially remove iterations of searching equal to the value of `k`, while each smaller list is double the size.

```python
# def contains_nearby_duplicate_d(self, nums: list[int], k: int) -> bool:
#         if k == 0:
#             return False
#         length = len(nums)
#         if k >= length - 1:
#             if length != len(set(nums)):
#                 return True
#             return False
#         else:
            for a in range(k, length - k):
                b = nums[a - k : a + k + 1]
                b.remove(nums[a])
                if nums[a] in set(b):
                    return True
#         return False
```

### contains_nearby_duplicate_e() & contains_nearby_duplicate_f()

These two solutions are the fastest of the group. The lesser manipulation of the given `nums` list seems to be the major reason. In these solutions, we're keeping a set/dictionary of seen values, which may be faster than list manipulation when called on by Python as a hash-set.

The only difference between these two is in whether to look that their `return True` condition as one line with an `and` or two `if`. There is a time difference, but it's not consistent. In a compiled language I'd consider some idea of a processor's handling of path prediction.

```python
# def contains_nearby_duplicate_e(self, nums: list[int], k: int) -> bool:
#         if k == 0:
#             return False
#         length = len(nums)
#         if k >= length - 1:
#             if length != len(set(nums)):
#                 return True
#             return False
#         else:
#             seen = {}
#             for i, value in enumerate(nums):
                if value in seen:
                    if i - seen[value] <= k:
                        return True
#                 seen[value] = i
#         return False
```

```python
# def contains_nearby_duplicate_f(self, nums: list[int], k: int) -> bool:
#         if k == 0:
#             return False
#         length = len(nums)
#         if k >= length - 1:
#             if length != len(set(nums)):
#                 return True
#             return False
#         else:
#             seen = {}
#             for i, value in enumerate(nums):
                if value in seen and i - seen[value] <= k:
                    return True
#                 seen[value] = i
#         return False
```
