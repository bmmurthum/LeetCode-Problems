# Remove Duplicated From Sorted Array II

**Description:**

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates **in-place** such that each unique element appears **at most twice**. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

**Examples:**

```text
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Overview

Our [solution](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/Remove-Duplicates-From-Sorted-Array-2/remove_duplicates_from_sorted_array_2.py) iterates once over the list `nums` while keeping two pointers. The `look_index` pointer is where we're currently looking for values, the `change_index` pointer is where we'll change a value. The `change_index` is left to its current position if we've found more than `mx` of this current value `current_num`. The `change_index` ends up being the numbers of integers in the list that are confirmed to be valid. Any after this index are garbage values.

```python
def remove_duplicates(self, nums: list[int]) -> int:
    """
    Removes elements from list, if there are more than 2 of that value. Keeps in relative order, handles in-place.

    If `b` items were removed, the list will be the same length, but with garbage values in the last `b` spaces.

    Args:
        `nums`: A list of integers. Sorted in non-decreasing order.
    Returns:
        `new_nums`: Now with removed items.
    """

    # Not possible changes to be made. Return.
    if len(nums) < 3:
        return len(nums)
    # Initial variables
    look_index = 0
    change_index = 0
    mx = 2
    current_num = nums[0]
    value_ct = 0
    # Walk through list with two pointers and some helper variables
    while look_index < len(nums):
        if nums[look_index] == current_num:
            value_ct += 1
        else:
            current_num = nums[look_index]
            value_ct = 1
        nums[change_index] = nums[look_index]
        if value_ct <= mx:
            change_index += 1
        look_index += 1
    return change_index
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and general confidence.

We ran this for my solution and two other's solutions.

We checked for:

- LeetCode's example cases
- Single item, two items. Which should be unchanged.
- Three identical items, three different items.
- Several items of a single value
- Positive and negative values
- A 1800 value generated list with two different values.

### Code Coverage

We received 100% code coverage on my method and others' from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run -m unittest
> coverage report
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
other_solution_2.py                           21      0   100%
other_solution_3.py                           18      0   100%
remove_duplicates_from_sorted_array_2.py      19      0   100%
test_cases.py                                 45      0   100%
test_unit_tests.py                           104      0   100%
--------------------------------------------------------------
TOTAL                                        207      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution `remove_duplicates()` and two other people's solutions `remove_duplicates_2()` and `remove_duplicates_3()`.

**Test 8:** A generated list of 1800 elements of two values.

Memory blocks used:

- `remove_duplicates()`: 416 blocks
- `remove_duplicates_2()`: 496 blocks
- `remove_duplicates_3()`: 476 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on two different test cases.

**Test 8:** A generated list of 1800 elements of two values.

- `remove_duplicates()`: 10.809 x 10^-5 sec
- `remove_duplicates_2()`: 6.327 x 10^-5 sec
- `remove_duplicates_3()`: 7.618 x 10^-5 sec

**Test 2:** LeetCode example case. Mixed list of 11 items.

- `remove_duplicates()`: 6.449 x 10^-7 sec
- `remove_duplicates_2()`: 4.693 x 10^-7 sec
- `remove_duplicates_3()`: 5.604 x 10^-7 sec

## Reflections

If I were to try to beat the efficiency of `other_solution_2.py` while still holding to the constraint of max-memory use of `O(1)`, I might make a `set()` of the values seen in `nums` to have the visibility to end iteration when we know that we've visited all possible values. This set would be the length of all distinct values in `nums` which is using more memory than these solutions, and at most half a copy of the list. Maybe this is considered `O(N/2)` memory, with the value of less than a forced `O(N)` runtime.

## Solution Variations

### other_solution_2.py

This solution has similar logic. Instead of two explicit pointers, there's the use of `enumerate()` which may have an efficiency bonus. Their use of a boolean `is_twice` is lovely, instead of my checking on a total `value_ct` of this current number. The benefit of `value_ct` is that my script can be easily expanded to run on looking for `3`, or any number, max of each value.

A big difference between mine and theirs is that they only write to the list in the case of when its needed. This is definitely an optimization.

```python
class Solution:
    def remove_duplicates_2(self, nums: list[int]) -> int:
        to_be_inserted_idx = 0
        is_twice = False
        prev = -987654321
        k = 0
        for _, v in enumerate(nums):
            if v == prev:
                if is_twice:
                    continue
                elif not is_twice:
                    k += 1
                    is_twice = True
                    nums[to_be_inserted_idx] = v
                    to_be_inserted_idx += 1
            else:
                k += 1
                is_twice = False
                nums[to_be_inserted_idx] = v
                to_be_inserted_idx += 1
                prev = v
        return k
```

### other_solution_3.py

This solution looks most similar to mine. It's like the other, but with `total = len(nums)` where `enumerate` would handle the value of this.

This script has unused `k = 0` and `start = 2`. It looks like they were considering starting their `range()` with that start value, but decided against it.

```python
class Solution:
    def remove_duplicates_3(self, nums: list[int]) -> int:
        total = len(nums)
        k = 0
        start = 2
        prev = -999999
        num_counter = 1
        index = 0
        for i in range(0, total):
            current = nums[i]
            if prev == current:
                num_counter += 1
            else:
                num_counter = 1
            if num_counter <= 2:
                nums[index] = nums[i]
                index += 1
            prev = current
        return index
```
