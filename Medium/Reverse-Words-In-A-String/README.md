# Ransom Note

**Description:**

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Example:**

```
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"

Input: s = "a good   example"
Output: "example good a"
```

## Overview

I made three solutions with slight variation, I'll look at the fastest performing method. The following describes the steps of the method.
- We strip spaces from the ends of string `s`
- While there are any `"  "` in `s` we replace them with a single space `" "`
- We use `.split(" ")` to grab the words into a list `words`
- We reverse the list
- We generate a new string to return from this list

```python
# My fastest solution
def reversewords_2(self, s: str) -> str:
    s = s.strip()
    while "  " in s:
        s = s.replace("  ", " ")
    words = s.split(" ")
    words.reverse()
    s = words[0]
    for w in range(1, len(words)):
        s = s + " " + words[w]
    return s
```

## Tests

**Unit Testing**

We implemented for this problem with `import unittest`. Tests were made for:
- Simple input with no double spaces or end spaces
- Input with several end spaces on either side
- Input with several padded internal spaces
- Input with a number inside


**Code Coverage**

We received 100% code coverage from the unit test using the `coverage.py` tool.
```
> coverage run unitTest.py
> coverage report -m 
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
reverseWordsInAString.py      11      0   100%
unitTest.py                   28      0   100%
--------------------------------------------------------
TOTAL                         39      0   100%
```

**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of the function with a string of `"     the   sky       is  blue     "`. We compare my three solutions with two other solutions, seen below.

My best solution `reversewords_3()` uses 25% more memory than the `reversewords_4()`.

Memory blocks used:

- `reversewords_1()`: 841 blocks
- `reversewords_2()`: 833 blocks
- `reversewords_3()`: 825 blocks
- `reversewords_4()`: 664 blocks
- `reversewords_5()`: 992 blocks


**Process Time Testing**

I used `timeit` to isolate the individual functions to run the input `"     the   sky       is  blue     "`. We compare my three solutions with two others.

My best solution `reversewords_2()` is 17% slower than the `reversewords_4()`.

- `reversewords_1()`: 4.653 x 10^-6 sec
- `reversewords_2()`: 4.251 x 10^-6 sec
- `reversewords_3()`: 4.536 x 10^-6 sec
- `reversewords_4()`: 3.549 x 10^-6 sec
- `reversewords_5()`: 4.044 x 10^-6 sec


## Reflections

I'll spend a minute looking again at the details of string and list manipulation.

This is my first implementation of `Black` and `Pylint` for code formatting.


## Solution Variations

This best-performing solution uses a most-naked version of `s.split()` to avoid any need for cleaning the string with `s.strip()` or removing double spaces. It also uses `.join()` to avoid iteration. It never calls for more memory outside of `words`, where my solutions create an internal instance of `s`.

`664 memory blocks` & `3.549 x 10^-6 sec`
```python
# Someone else's solution
def reversewords_4(self, s: str) -> str:
    words = s.split()
    words.reverse()
    return " ".join(words)
```

`992 memory blocks` & `4.044 x 10^-6 sec`
```python
# Someone else's solution
def reversewords_5(self, s: str) -> str:
        r = s.strip().split(" ")
        r1 = r[::-1]
        r2 = [i for i in r1 if i != ""]
        s2 = " ".join(r2)
        return s2
```