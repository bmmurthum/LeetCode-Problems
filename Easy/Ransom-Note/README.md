# Ransom Note

**Description:**

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

- `1 <= ransomNote.length`, `magazine.length <= 105`
- `ransomNote` and `magazine` consist of lowercase English letters.

**Example:**

```
Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
```

## Overview

My solution creates a new set `uniqueLetters` out of the `ransomNote` to grab which unique letters we need. For each one of these letters `letter` we see if the count between the `ransomNote` list and `magazine` list is the same. If we find a different count, we break and return `False`. If we don't find a difference, we return `True`. We'll only have to iterate at max for as many letters as there are in the alphabet.

```python
class Solution:
    def canConstruct_1(self, ransomNote: str, magazine: str) -> bool:
        uniqueLetters = set(ransomNote)
        for letter in uniqueLetters:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
```

## Tests

**Unit Testing**

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Ransom-Note/unitTest.py) for this problem with `import unittest`. Tests were made for:
- Single letter not matching
- Single letter matching
- Not enough desired letters in `magazine`
- No letters in `magazine` to create the ransom note
- To show that we did not design to handle spaces `"hi mom"`


**Code Coverage**

We received 100% code coverage from the unit test using the `coverage.py` tool.
```
> coverage run unitTest.py
> coverage report -m 
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
ransomNote.py       7      0   100%
unitTest.py        38      0   100%
---------------------------------------------
TOTAL              45      0   100%
```

**Memory Usage Testing**

I used `tracemalloc` to look at peak memory block usage during the running of the function with a string of about 30 characters that returns `True`. We compare mine with four other solutions, seen below. [Memory Tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Ransom-Note/memoryTest.py)

My solution uses 6.4x the memory of the `canConstruct_5()`? Oh good heavens. The creation of the `uniqueLetters` set, for sure. I figured the lesser iteration count would be worth something.

Memory blocks used:

- `canConstruct_1()`: 3144 blocks
- `canConstruct_2()`: 768 blocks
- `canConstruct_3()`: 1584 blocks
- `canConstruct_4()`: 503 blocks
- `canConstruct_5()`: 495 blocks


**Process Time Testing**

I used `timeit` to isolate the individual functions to run many times with an identical test case. We compare my solution with four others. [Speed Tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Ransom-Note/timeTest.py)

The `canConstruct_5()` method is 32% faster than my `canConstruct_1()`.

- `canConstruct_1()`: 6.700 x 10^-6 sec
- `canConstruct_2()`: 4.561 x 10^-6 sec
- `canConstruct_3()`: 6.802 x 10^-6 sec
- `canConstruct_4()`: 6.690 x 10^-6 sec
- `canConstruct_5()`: 4.536 x 10^-6 sec


## Reflections

Looking at these speed and memory usage variations, to have a built understanding of what Python library methods are faster must be a help. Also, doing these A/B tests on a battery of different use cases and solutions must definitely produce some better optimization.


## Solution Variations

`768 memory blocks` & `4.561 x 10^-6 sec`
```python
def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
    magazine = [letter for letter in magazine]
    for letter in ransomNote:
        if letter not in magazine:
            return False
        else:
            magazine.remove(letter)
    return True
```

`1584 memory blocks` & `6.802 x 10^-6 sec`
```python
def canConstruct_3(self, ransomNote: str, magazine: str) -> bool:
    letter_count_m = dict()
    for char in magazine:
        if char in letter_count_m.keys():
            letter_count_m[char]+=1
        else:
            letter_count_m[char] = 1
    for char in ransomNote:
        if char not in letter_count_m:
            return False
        if letter_count_m[char]<=0:
            return False
        else:
            letter_count_m[char]-=1
    return True
```

`503 memory blocks` & `6.690 x 10^-6 sec`
```python
def canConstruct_4(self, ransomNote: str, magazine: str) -> bool:
    for let in ransomNote:
        if let in magazine:
            ind = magazine.find(let)
            magazine = magazine[:ind] + magazine[ind + 1:]
        else:
            return False
    return True
```

This higher performing method iterates through each character in `ransomNote`, sees if there is a case of it in `magazine`, if there is, remove ones and continues.

It never creates any new variables. `replace()` rather than `remove()` is likely faster in not telling the list to change indexes. Also, it never `counts` any characters in the list, which may be a heavier request than `in`.

`495 memory blocks` & `4.536 x 10^-6 sec`
```python
def canConstruct_5(self, ransomNote: str, magazine: str) -> bool:
    for ch in ransomNote:
        if ch in magazine:
            magazine = magazine.replace(ch,"",1)
        else:
            return False
    return True
```

