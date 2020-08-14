# Longest Substring Without Repeating Character

**Description:**

Given a string, find the length of the longest substring without repeating characters. Solution written in Python 3.8.5.

**Example:**
```
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

## Reflections

My approach to this was with entry Python knowledge. I put little effort to optimization in terms of memory use and of O() time complexity. My aim was to complete the requirements quickly with high readability.

I decided to go with `camelCase` for readability and not simple unrelated variable names. I figure that plays into the social code of Python.

## Further Inquiry

With another run at this problem, I would aim to store indexes of critical positions in order to avoid backward iteration. I would also aim to avoid hard-coding for edge cases and initial states.

## Sample Inputs

**Case 1:**
```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Case 2:**
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

**Case 3:**
```
Input: "ab"
Output: 2
Explanation: The answer is "ab", with the length of 2.
```

**Case 4:**
```
Input: ""
Output: 0
Explanation: The answer is "", with the length of 0.
```

**Case 5:**
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```
