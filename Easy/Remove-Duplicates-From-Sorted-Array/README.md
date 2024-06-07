# Remove Duplicates From Sorted Array

**Description:**

Given an integer array `nums` sorted in **non-decreasing** order, remove the duplicates **in-place** such that each unique element appears only **once**. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**Example:**

The blanks in the output lists are to suggest any value can be there acceptably.
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

## Overview

My solution to this iterates through the given list `nums` while keeping track of the value of the last different value `lastValue` and its index `ptr`. This pointer `ptr` is incremented everytime we see a new unique value.

At the end of the `nums` list, we know that `ptr` is equal to the number of unique values we saw. We return `ptr`.

By the end of our incrementing, the initial `nums` list has been changed in the process, in that it's called by reference as a mutable object. This list being changed to an non-descending ordered list is desired by the requirements.

```python
def removeDuplicates_1(self, nums: list[int]) -> int:
    ptr = 1
    lastValue = nums[0]
    for i in range(1,len(nums)):
        if nums[i] != lastValue:
            nums[ptr] = nums[i]
            lastValue = nums[i]
            ptr += 1
    return ptr
```

We must increment to each item in the list in case there's another unique value at the end, making this at optimally O(n).


## Tests

**Unit Testing**

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Remove-Duplicates-From-Sorted-Array/unitTest.py) for this problem with `import unittest`. Tests were made for:
- Two simple cases
- Both negative and positive values
- A single value
- Many middle of sorted list duplicates

**Memory Usage Testing**

I wanted to look into optimization, so I wrote up three other algorithm options for this problem with some observation of others' solutions. I used `tracemalloc` to look at peak memory block usage during the running of the function for each of the four similar functions. [Memory Tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Remove-Duplicates-From-Sorted-Array/memoryTest.py)

```python
import tracemalloc
nums = [1,2,3,4]
tracemalloc.start()
v = s.removeDuplicates_1(nums)
print("Peak Memory Blocks Used: " + str(tracemalloc.get_traced_memory()[1]))
tracemalloc.stop
```

- `removeDuplicates_1()`: 400 blocks
- `removeDuplicates_2()`: 392 blocks
- `removeDuplicates_3()`: 1184 blocks
- `removeDuplicates_4()`: 1224 blocks

**Process Time Testing**

I used Python's `timeit` library to isolate the individual functions to run with an identical test case. [Speed Tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Remove-Duplicates-From-Sorted-Array/timeTest.py) suggest that `removeDuplicates_4()` is the fastest, being 14% faster than `removeDuplicates_3()` at the slowest.

- `removeDuplicates_1()`: 3.889 x 10^-6 sec
- `removeDuplicates_2()`: 3.657 x 10^-6 sec
- `removeDuplicates_3()`: 3.935 x 10^-6 sec
- `removeDuplicates_4()`: 3.439 x 10^-6 sec

**Solution Variations**

Similar to my solution, but without holding a `lastValue` for comparision. It looks like the 8 memory block difference is in that holding `lastValue` variable I used. Some notable time difference, maybe spent in assigning and comparing that value.
```python
def removeDuplicates_2(self, nums: list[int]) -> int:
    count = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[count] = nums[i]
            count += 1
    return count
```

Uses a `set()` casting to remove duplicates--feels like avoiding the challenge of the question. Then they iterate to set the `nums` list to these values. It uses three times the memory and is a pinch slower than my algorithm. It looks like in addition to the `nums` list, `setNums` adds another similar chunk, and maybe `sorted` has a temporary call for memory.  
```python
def removeDuplicates_3(self, nums: list[int]) -> int:
    setNums = set(nums)
    setNums = sorted(setNums)
    j = 0
    for i in setNums:
        nums[j] = i
        j = j + 1
    return j
```

This one I made based off of the last one to try to take advantage of `nums` being mutable to avoid the iteration. This one being the fastest and using the most memory is fun. It triples the memory usage, so watch for that on big lists?
```python
def removeDuplicates_4(self, nums: list[int]) -> int:
    setNums = list(set(nums))
    nums.clear()
    nums.extend(setNums)
    return len(nums)
```


## Reflections

I want to look at how people are automating these sorts of tests. I would feel more comfortable with larger lists being tests and a battery of test values for each speed/memory test.

And certainly I would save so much time by not writing these tests.
