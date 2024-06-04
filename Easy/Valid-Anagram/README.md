# Valid Anagram


**Description:**

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints: 
- `1 <= s.length, t.length <= 5 * 104`
- `s` and `t` consist of lowercase English letters.


**Example:**
```
Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False
```


## Overview

My solution iterates through each of the given words looking at each letter and adding a hashed `hash("a")` output of that letter to a sum. This sum should be equal if the letters are the same, regardless of order. This hash could be low quality for optimization so long as each letter gave a unique value and gave sufficient space between character values to avoid multiples of one letter suggesting another specific letter is inside. We return `True` if the hashes are equal and the string length is the same.

```python3
for I in range(0,len(s)):
    sHash = sHash + hash(s[I])
```

My first run at this problem had a rudimentary hashing function of the total words on this basis, where each letter is outputted as an integer `ord("a")`, then this is added to the sum. This came to a conflict on the case of `"bb"` and `"ac"` where both totals were the same. 

```python3
sHash = 0
tHash = 0
for I in range(0,len(s)):
    sHash = sHash + (ord(s[I]) - ord("a"))
for J in range(0,len(t)):
    tHash = tHash + (ord(t[J]) - ord("a"))
```

Another variation on the hashing that I thought about would be a prime-number multiplication design, where each letter is associated with a prime number and these are multiplied to a total to be compared. I figured it was too laborous and there may be an issue in integer length in the given constraints. Certainly, using a given python library is reasonable idea, unless we're in the wheel invention business.


We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Valid-Anagram/test.py) for this problem with `import unittest`. Tests were made for:
- A variety of correct cases
- A variety of incorrect cases
- Longer, shorter and missing strings in either position
- Single letter cases

## Reflections

Certainly having exposure to a collection of Python default methods allows for a quick run on these sorts of questions. That's the value here.