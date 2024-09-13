# Majority Element

**Description:**

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Examples:**

```text
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Overview

My [solution](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Majority-Element/majority_element.py) finds a set of the distinct different values in the list, then counts how many of each. Whichever is more than half, gets returned. I want to engrain in myself that I should be using the Python libraries when possible for the C-optimization in speed.

The second solution I did would be notably readable, but not optimized in any clever way, outside of its knowing to stop counting if one of its counted items is above `count_to_pass = len(nums) // 2`.

**First Solution:**

```python
def majority_element(self, nums: list[int]) -> int:
    """
    Returns the value of the items that are a majority of the items in the list.
    It's assumed that there is an item that this is the case.

    Args:
        `nums`: The given list to look through.
    Returns:
        `majority_item`: The value of the item of majority. `None` if no majority item.
    """
    nums_set = set(nums)
    for i in nums_set:
        if nums.count(i) > len(nums) // 2:
            return i
```

**Second Solution:**

```python
def majority_element_2(self, nums: list[int]) -> int:
    count_to_pass = len(nums) // 2
    count_dict = {}
    for _, item in enumerate(nums):
        if count_dict.get(item) is None:
            count_dict[item] = 1
        else:
            count_dict[item] = count_dict[item] + 1
        if count_dict[item] > count_to_pass:
            return item
```


## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and general confidence.

We ran this for my two solutions and two other's solutions.

We checked for:

- LeetCode's example cases
- Two items in list, identical.
- One item.
- 5000 long generated list.

At first, I had tests for invalid cases. The problem didn't call to handle this constraint. When I wanted to see other people's solutions, then didn't handle these issues and I dropped the tests.

- No items meeting a majority.
- Matching number of two items.

### Code Coverage

We received 100% code coverage on my method and others' from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run -m unittest
> coverage report
Name                  Stmts   Miss  Cover
-----------------------------------------
majority_element.py      15      0   100%
other_solution_2.py      11      0   100%
other_solution_3.py      14      0   100%
test_unit_tests.py       68      0   100%
testcases.py             23      0   100%
-----------------------------------------
TOTAL                   131      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solutions `majority_element()` and `majority_element_2()` against two other people's solutions `majority_element_3()` and `majority_element_4()`.

**Test 7:** A generated list of 5000 elements of three values.

Memory blocks used:

- `majority_element()`: 688 blocks
- `majority_element_2()`: 780 blocks
- `majority_element_3()`: 40424 blocks
- `majority_element_4()`: 432 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on a test cases.

**Test 7:** A generated list of 5000 elements of three values.

- `majority_element()`: 0.365 x 10^-4 sec
- `majority_element_2()`: 2.546 x 10^-4 sec
- `majority_element_3()`: 1.477 x 10^-4 sec
- `majority_element_4()`: 1.321 x 10^-4 sec

## Reflections

Using Python's libraries where applicable is fair, feels like less of an algorithm exercise at this point and more of a lets-not-recreate-wheel meditation.

My `majority_element_2()` uses a simple dictionary with counting. This is about half as fast as the others' solutions. I didn't attempt for much optimization here and I'm ok with that.

## Solution Variations

### other_solution_2.py

```python
class Solution:
    def majority_element_3(self, nums: list[int]) -> int:
        counter, majority = 1, nums[0]
        for num in nums[1:]:
            if num == majority:
                counter += 1
            else:
                counter -= 1
            if not counter:
                majority = num
                counter += 1
        return majority
```

### other_solution_3.py

```python
class Solution:
    def majority_element_4(self, nums: list[int]) -> int:
        count = 0
        res = 0
        for i in nums:
            if count != 0:
                if res != i:
                    count -= 1
                else:
                    count += 1
            else:
                if res == i:
                    count += 1
                else:
                    res = i
                    count += 1
        return res
```
