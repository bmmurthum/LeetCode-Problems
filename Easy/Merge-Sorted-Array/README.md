# Merge Sorted Array

**Description:**

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. nums2 has a length of `n`.


**Example:**
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

## Overview

My solution puts three total pointers on the two lists. One for the result, one for each of the values we are currently considering. With these pointers we compare which value is greater, then commit that value to the result by copying this value to the position of the result-pointer.

Unique cases of empty lists are handled before any iterations.

We also handle cases of one of the list pointers coming to the beginning of its list before the other.

We implemented unit-tests for this problem using a [second file](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Merge-Sorted-Array/test.py) with `import unittest`. Tests were made for:
- Varieties of empty lists
- One list longer than other
- Values of one list encapsulating the other
- All negative values
- Zeroes within the solution
- Exclusively zeroes

## Reflections

This exercise seems setup to be intended for pointer exercise and iterating through lists. I see some solutions that have a sort() involved. That's no good.

```
nums1[m:] = nums2
nums1.sort()
```

## Test Cases

**Case 1:**
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

**Case 2:**
```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
```

**Case 3:**
```
Input: nums1 = [0,0,0,0,0,0,0], m = 0, nums2 = [1,3,3,4,5,6,10], n = 7
Output: [1,3,3,4,5,6,10]
```