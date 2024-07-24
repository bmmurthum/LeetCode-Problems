# Game of Life

**Description:**

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Constraints:**

- `1 <= s.length <= 5 * 104`
- `t.length == s.length`
- `s and t consist of any valid ascii character.`

**Examples:**

```text
Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
```

## Overview

My solution builds a dictionary `found` as we iterate through both strings simultaneously. When looking at a letter from each string `a` and `b`, if both letters are not found in their respective key or value in `found`, we know to add this pair to the dictionary.

If one of the values is in our dictionary and not the other, we know we've bumped into a case that makes these two string non-isomorphic, and we can return `False`.

We can also return `False` when the key has been seen but the value doesn't match the found character in `t`.

```python
class Solution:
    """Problem given by LeetCode."""

    def is_isomorphic(self, s: str, t: str) -> bool:
        """
        Tells us if two strings are isomorphic to each other.

        Args:
            `s`: One string
            `t`: Another string
        Returns:
            `True/False`: If strings are isomorphic.
        """

        found = {}
        for a, b in zip(s, t):
            # If both have not been seen.
            if a not in found.keys() and b not in found.values():
                found[a] = b
            # This key/value is recorded, but not the other.
            elif (a not in found.keys() and b in found.values()) or (
                a in found.keys() and b not in found.values()
            ):
                return False
            # Current value doesn't match
            elif a in found.keys() and found[a] != b:
                return False
        return True
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and general confidence.

We ran this for my solution `is_isomorphic` and two other people's solutions.

We checked for:

- LeetCode's three example cases.
- A single letter
- Lowercase and uppercase being recognized differently
- Using non-alpha ASCII characters
- Using the whole alphabet
- Using the whole alphabet, twice
- Using the whole alphabet, with false letter

### Code Coverage

We received 100% code coverage on my methods from the unit-test using the `coverage.py` tool.

The lower coverage on the others' methods comes from the unused check for the two strings not being the same length.

```PowerShell
> coverage run -m unittest
> coverage report
Name                      Stmts   Miss  Cover
---------------------------------------------
isomorphic_strings.py        11      0   100%
isomorphic_strings_2.py      13      1    92%
isomorphic_strings_3.py      16      1    94%
test_unittests.py           100      0   100%
testcases.py                 46      0   100%
---------------------------------------------
TOTAL                       186      2    99%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution `is_isomorphic()` against the others' solutions.

**Test 9:** Alphabet twice, with wrong letter match at end.

- `is_isomorphic()`: 1648 blocks
- `is_isomorphic_2()`: 2416 blocks
- `is_isomorphic_3()`: 3144 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on a test cases.

**Test 9:** Alphabet twice, with wrong letter match at end.

- `is_isomorphic()`: 10.243 x 10^-6 sec
- `is_isomorphic_2()`: 3.626 x 10^-6 sec
- `is_isomorphic_3()`: 9.823 x 10^-6 sec

## Reflections

I'm happy with my solution. If I were to do more, I'd look to do something more hash-map focused for efficiency. Any lessening of checking on the lists and generating the key/value lists would be a good direction.

## Solution Variations

### isomorphic_strings_2.py

Both of the following solutions add a watch for if the two strings are not the same length `if len(s) != len(t): return False`, but the constraints of the problem say that this will never be given. It's a nice safety for low cost, but is uncalled for.

This solution, being the fastest of the three does identical logic to mine, but uses two matching dictionaries instead of a single dictionary. My difference in performance could be at the moment of checking `a not in found.keys()` a few different ways.

```python
class Solution:
    def is_isomorphic_2(self, s: str, t: str) -> bool:
        map_s_t = {}
        map_t_s = {}
        if len(s) != len(t):
            return False
        for cs, ct in zip(s, t):
            if ct not in map_t_s and cs not in map_s_t:
                map_t_s[ct] = cs
                map_s_t[cs] = ct
            elif map_t_s.get(ct) != cs or map_s_t.get(cs) != ct:
                return False
        return True
```

### isomorphic_strings_3.py

This method works by searching on each unique character in `s` and making sure that character always has the same matching index in `s` and partnered `t` when looking through to find all the cases of that character.

```python
class Solution:
    def is_isomorphic_3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_unique = set(s)
        for s_char in s_unique:
            start = 0
            s_index = s.find(s_char, start)
            t_char = t[s_index]
            while s_index != -1:
                start = s_index + 1
                s_index = s.find(s_char, start)
                t_index = t.find(t_char, start)
                if s_index != t_index:
                    return False
        return True
```
