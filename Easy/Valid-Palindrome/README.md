# Merge Two Sorted Lists

**Description:**

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false

Input: s = " "
Output: true
```

## Overview

For traversal of the intial string, we setup `r` and `l` as index pointers. While the right pointer `r` is to the right of `l` we continue on. If, while traversing, one of the characters of `s[r]` or `s[l]` is not alpha-numeric, we move the pointer and skip to the beginning of the iteration. If we come to have two valid characters, we consider them as lowercase and see if they are the same value; if true, we move both pointers, if false, we return `False`. If we haven't bumped into a incorrect case by the end of traversal, return `True`.  

This intentionally avoids manipulating the string `s` for efficiency, as removal of a character would cause each character to have to be shifted. We also tried to minimize any new creation of temporary lists.

If there is a smaller-memory sized variable type for pointers, I may use that. Though it'd only change anything in performance if the memory block size induced more than one call to memory, which is also hardly an issue.

```python
# My solution
def is_palindrome_1(self, s: str) -> bool:
        r = len(s) - 1
        l = 0
        while r - l > 0:
            if s[r].isalnum() is False:
                r -= 1
                continue
            elif s[l].isalnum() is False:
                l += 1
                continue
            elif s[r].lower() == s[l].lower():
                r -= 1
                l += 1
            else:
                return False
        return True
```

## Tests

**Unit Testing**

We implemented unit-tests for this problem with `import unittest`. We checked for:
- Simple case with spaces involved
- Case with "," and ":" and varied capitalization
- A single space " ", to return `True`
- Larger string with only non-alpha-numeric characters, to return `True`
- A single valid character, to return `True`
- Valid string of numbers
- Invalid string of numbers


**Code Coverage**

We received 100% code coverage on `valid_palindrome.py` from the unit test using the `coverage.py` tool.

```
> coverage run unitTest.py
> coverage report -m 
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
unit_test.py             48      0   100%
valid_palindrome.py      16      0   100%
---------------------------------------------------
TOTAL                    64      0   100%
```

**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of the function. We compare my solution with two other solutions, seen below.

My solution `is_palindrome_1()` uses memory only for the left and right pointers, which I am happy with.

Memory blocks used:

- `is_palindrome_1()`: 100 blocks
- `is_palindrome_2()`: 392 blocks
- `is_palindrome_3()`: 2507 blocks


**Process Time Testing**

I used `timeit` to isolate the individual functions on the same input.

My solution `is_palindrome_1()` is 12% faster than the next fastest `is_palindrome_2()` with the case of `"123456788889888888754321"`.

- `is_palindrome_1()`: 0.848 x 10^-6 sec
- `is_palindrome_2()`: 0.957 x 10^-6 sec
- `is_palindrome_3()`: 0.963 x 10^-6 sec


## Reflections

I want to do tests with variations of cases to compare memory usage and performance with more integrity.

## Solution Variations

`is_palindrome_2()` creates a new string by chain of `join`, loop with conditions, and `lower` in one line. It feels readable. It's all in one line. Love it.

Then they check that the string is equal to the string in reverse. Love that.

`392 memory blocks` & `0.957 x 10^-6 sec`
```python
# Someone else's solution
def is_palindrome_2(self, s: str) -> bool:
    str1 = "".join([i for i in s if i.isalnum()]).lower()
    if str1 == str1[::-1]:
        return True
    else:
        return False
```

`is_palindrome_3()` uses the regular expression library to create a new string `cleaned` with non-alpha-numeric characters in `s` replaced with an empty character. That they used regex leaves this more flexible for some other cases, which is nice.

Then they iterate with two pointers to compare values as I did.

`2507 memory blocks` & `0.963 x 10^-6 sec`
```python
# Someone else's solution
import re
def is_palindrome_3(self, s: str) -> bool:
    cleaned = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True
```
