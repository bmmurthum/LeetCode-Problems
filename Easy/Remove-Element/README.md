# Remove Element

**Description:**

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

Change the array nums such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.

Return `k`.

**Example:**

The blanks in the output lists are to suggest any value can be there acceptably.
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
```

## Overview

We understand that our returned integer `pnt` is not the only requirment of this method. The given list `nums` is meant to be changed as well. With Python, lists, as a mutable type, are passed to our method by reference and any changes to them will be kept outside of the scope of our method.

In `removeElement` we set up a pointer `pnt` that moves forward as we iterate through the list. When we observe a value that we'd like to keep, we put that value at the index of `pnt`, then increment `pnt`.

```python3
def removeElement(self, nums: list[int], val: int) -> int:
    pnt = 0
    for i in range(0,len(nums)):
        if nums[i] != val:
            nums[pnt] = nums[i]
            pnt += 1
    # The LeetCode Test-Cases require you pop() from your list
    # even though its requirements describe to not do this.
    # for j in range(0,len(nums)-pnt):
    #     nums.pop()
    return pnt
```


## Tests

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Remove-Element/test.py) for this problem with `import unittest`. Tests were made for:
- Two simple cases
- An incrementing valued list, our removal at the end
- An incrementing valued list, our removal at beginning
- A removal of all the list values except one at the end
- A removal of all the list values except one at the beginning
- A removal of all items in the list

Because the requirements of this problem called for specific end results beyond the return value `k`, our `pnt`, I set up each test to check for four conditions.
- Our newly changed `nums` list was the same length as before.
- The beginning `k` values of `nums` didn't contain the removed `val`
- The beginning `k` values had the same number of each unique other value.
- The returned `k` value was correct

## Reflections

The requirements and constraints suggest that a returned list should be the same length as before running our method `removeElement`. The submission system rejects this, waiting for a shortened list with the removed elements gone. We used `pop()` for this, but did not design our testing suite for that.
