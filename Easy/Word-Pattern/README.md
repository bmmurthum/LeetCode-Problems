# Word Pattern

**Description:**

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.


**Example:**
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: True

Input: pattern = "abba", s = "dog cat cat fish"
Output: False

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: False
```

## Overview

My solution splits the given string into words with the `" "` delimiter, then iterates through the `pattern` string in parallel with the word list. If a new letter is seen for the first time in the `pattern` string, we add the word that should be associated with it. If that letter has been seen before, we check that the current word in the word list matches correctly.

The constraints of the problem don't mention anything about mismatch of number of letters in the pattern with word-list length. We handle that case.

## Reflection

On submission, I saw that I missed the case of two different letters refering to the same string. I fixed this with a check through the values of my dictionary.

```
Input: pattern = "abba", s = "dog dog dog dog"
Output: False
```

Some other people's submissions used a combination of `zip()` and `set()` to create three sets and then compare lengths as a way to check to discrepancies between them. The use of `zip()` to do something like a dictionary matching words with their letter, like in my sollution. The use of `set()` to disallow duplicate cases. They then observe the `length()` of these sets to be equal for a success-case.

For a moment, this feels like a lossy situation that may be a problem: `abbca` becomes `abc`. As long as the tuples of the `zip()` match with these removals, we don't need to care about the pattern as much as caring that for each letter there is one word matched.

```
def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        words = s.split(" ")
        if len(p) != len(words):
            return False
        return len(set(zip(p, words))) == len(set(p)) == len(set(words))
```


## Test Cases

We implemented unit-tests for this problem using a [second file](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Word-Pattern/test.py) with `import unittest`. Tests were made for:
- Correct simple case
- Incorrect simple case
- Incorrect case, with all single letter pattern
- Correct case with all unique pattern and words
- Correct case with a mirroring pattern
- Longer correct case with unique double at end
- Incorrect case in which pattern length doesn't match with word count