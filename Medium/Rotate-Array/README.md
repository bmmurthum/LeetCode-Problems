# Rotate Array

**Description:**

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.
- Could you do it in-place with `O(1)` extra space?

**Example:**

The blanks in the output lists are to suggest any value can be there acceptably.
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

## Overview

I aimed to find a solution to the problem in-place with `O(1)` extra memory. For my solution we use two holders, `holder1` and `holder2`, to replace values between the one we're visiting and the next as we iterate through the list. Our next value in the `nums` list is `k` values increased from the current, unless we would go over `nums` length, in which we use `%` to figure where we loop over to the beginning.

We use `start` to keep a note on the index that we started on to check if we bump into it again. If we do, we start on the next value to the right and set this as the new `start`.

We handle simple cases at the top to avoid iteration if possible.

We don't return a list because this function is meant to directly change the reference of the given list.

```python
def rotate_1(self, nums: list[int], k: int) -> None:
        '''
        Rotates `nums` list `k` integers to the right. `k` is expected to be a non-negative integer.
        '''
        # Handling simple cases
        if len(nums) == 1:
            return
        if len(nums) == k:
            return
        if k == 0:
            return

        # Hold first value
        holder1 = nums[0]
        # Index of current position
        j = 0
        # Index of the value we started at
        start = 0
        for i in range(len(nums)):
            # Hold next value, to replace
            holder2 = nums[(k+j) % len(nums)]
            # Replace next value with first value
            nums[(k+j) % len(nums)] = holder1
            # Switch this new value to "first value" holding
            holder1 = holder2
            # If at end of loop and next-spot has been visited, move one space to right, and keep going.
            if (k+j) >= len(nums) and (k+j) % len(nums) == start:
                start += 1
                j = ((k+j) % len(nums)) + 1
                holder1 = nums[j]
            # Next spot is "k" items to the right.
            else:
                j = (k+j) % len(nums)
```

## Tests

**Unit Testing**

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/Rotate-Array/unitTest.py) for this problem with `import unittest`. Tests were made for:
- No rotation
- List with one item rotated three times
- List rotated the same amount as its length
- All cases on a list of length six
- A couple cases of a prime-lengthed list


**Code Coverage**

We received 100% code coverage from the unit test using the `coverage.py` tool.
```
> coverage run unitTest.py
> coverage report -m 
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
rotateArray.py      20      0   100%
unitTest.py         62      0   100%
----------------------------------------------
TOTAL               82      0   100%
```

**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of the function with a list of 10 values. We compare mine with two other solutions, seen below. [Memory Tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/Rotate-Array/memoryTest.py)

Memory blocks used:

- `rotate_1()`: 400 blocks
- `rotate_2()`: 392 blocks
- `rotate_3()`: 552 blocks


**Process Time Testing**

I used `timeit` to isolate the individual functions to run many times with an identical test case. We compare my solution with two others. My speed difference is likely in the logic being within the iteration. [Speed Tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/Rotate-Array/timeTest.py)

- `rotate_1()`: 4.411 x 10^-6 sec
- `rotate_2()`: 2.799 x 10^-6 sec
- `rotate_3()`: 2.816 x 10^-6 sec


## Reflections

I was stuck on the case of `k` rotation being divisible by the length of `nums` for a little while. Where my `start` value at first was considered to be a static zero.

In comparison these following solutions, I put much of my logic inside the iteration which is the cause of the difference in speed. My program looks to be an exercise of pointers and clever iteration, where theirs are applied list manipulations.

## Solution Variations

This solution `rotate_2()` used 392 blocks of memory to my 400. It was 35% faster as well.

They reduce the `k` shift to be within the list length `l` if it happens to be larger than the length. Then they use a clever list selection to put what was behind `k` in the beginning up to `k` and vice versa.

This avoids my `O(N)` iteration through the list by using list methods.
```python
def rotate_2(self, nums: list[int], k: int) -> None:
        l = len(nums)
        k = k % l
        if k == 0:
            return
        nums[ :k], nums[k: ] = nums[l-k: ], nums[ :l-k]
        return
```

This solution `rotate_3()` used 552 blocks of memory to my 400. It was also about 35% faster.

This method does the same process as the last, generally. It doesn't use a variable for `len(nums)`. It creates a new list `rotated` to hold the variables of the new placements in the same way as the last, then applies this to `nums` in iteraton.

I like their use of `enumerate()`. My `for` loop doesn't use it's looping variable, but is used exclusively for the calling of other logic, so I don't know that I would apply `enumerate()` in the same way. 
```python
def rotate_3(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        rotated=nums[len(nums)-k:]+nums[:len(nums)-k]
        for i,number in enumerate(rotated):
            nums[i]=number
```
