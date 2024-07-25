# Longest Consecutive Sequence

**Description:**

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

**Constraints:**

- `0 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

**Examples:**

```text
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

## Overview

The anchor of our solution is that we create a set of the `nums` list to be able to see if a value is `in` the set with quick hash-table access.

We iterate through the given `nums` to see if there exists a number in our set that is one less than our value. If this is `True` we know that this value is a start of a consecutive chain. We then count a total of how many values are one above the last in our set. We return the `max_length` found in this process.

```python
class Solution:
    """Problem given by LeetCode."""

    def longest_consecutive_a(self, nums: list[int]) -> int:
        """
        Finds the longest consecutive chain of values in an unordered list. O(n) time complexity.

        Args:
            `nums`: The list of numbers to look through.
        Returns:
            `max_length`: Max count of integers that are value neighbors.
        """

        # Set to allow for hash-table speed calls.
        num_set = set(nums)
        max_length = 0
        for start in nums:
            if start - 1 not in num_set:
                end = start + 1
                while end in num_set:
                    end += 1
                max_length = max(max_length, end - start)
        return max_length
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's two example cases.
- An empty list
- A simple case
- One item in list
- Two of the same number in list
- Two different numbers
- 20-long chain with values before and after in list and above and below in value.

```text
** Unit Tests **

Unit Tests Ran: 8
Methods Tested: 3
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 100% code coverage on my method with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report
Name                                Stmts   Miss  Cover
-------------------------------------------------------
call_tests.py                          13      0   100%
longest_consecutive_sequence.py        11      0   100%
longest_consecutive_sequence_2.py      22      1    95%
longest_consecutive_sequence_3.py      19      0   100%
memory_tests.py                        48      0   100%
testcases.py                           33      0   100%
time_tests.py                          42      0   100%
unit_tests.py                         108      0   100%
-------------------------------------------------------
TOTAL                                 296      1    99%
```

Missing coverage in `longest_consecutive_sequence_2.py` is in checking for a value below the current looked-at value while iterating the set `x`. This is never seen because the set seems ordered, though Python doesn't guarantee this being the case.

```python
if n - 1 in x:
    continue
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solutions against the others' solutions.

```text
** Memory Tests **

Testcase 8: 20-long chain. 30 total values.
    longest_consecutive_a(): 2888 blocks
    longest_consecutive_2(): 5848 blocks
    longest_consecutive_3(): 2888 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a test case. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 8: 20-long chain. 30 total values.
    longest_consecutive_a() runtime: 1.8156e-03 sec
    longest_consecutive_2() runtime: 3.5997e-03 sec
    longest_consecutive_3() runtime: 1.4927e-03 sec
```

## Reflections

The LeetCode discussion boards were all over about what counts for O(n) time in this problem. There's suggestion that any use of `sort` excludes the O(n) time requirement, which excludes the solution that beats mine in performance ([1](https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/)). The conversion of the `nums` list to a set feels like it would cost O(n) time in itself ([2](https://www.geeksforgeeks.org/time-complexity-of-a-list-to-set-conversion-in-python/)).

## Solution Variations

### longest_consecutive_sequence_2.py

The keeping of a `visited` set likely helps their speed. As well as iterating through the potentially smaller set `x` instead of the given `nums`.

The `lk` and use of `defaultdict` is unclear and I wish I'd see some comments or more verbose variable names.

```python
class Solution:
    def longest_consecutive_2(self, nums: list[int]) -> int:
        x = set(nums)
        lk = defaultdict(int)
        visited = set()
        result = 0
        for n in x:
            if n in visited:
                continue
            if n - 1 in x:
                continue
            visited.add(n)
            l = 1
            original_n = n
            while (n := n + 1) in x:
                l += 1
                visited.add(n)
            l += lk[original_n - 1]
            lk[n - 1] = l
            result = max(result, l)
        return result
```

### longest_consecutive_sequence_3.py

The `nums = list(set(nums))` to remove duplicates and do a soft sort is interesting. Python's `set` is unordered, but does some of the work it appears.

The `nums.sort()` is to be avoided in that its time-costly. At small-length `nums` maybe it's cost effective for its use.

```python
class Solution:
    def longest_consecutive_3(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        longest = 0
        length = 0
        prev = -1
        for num in nums:
            if prev + 1 == num:
                length += 1
            else:
                if length > longest:
                    longest = length
                length = 1
            prev = num
        if length > longest:
            longest = length
        return longest
```
