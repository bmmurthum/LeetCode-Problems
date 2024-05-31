# Number of Steps to Reduce a Number in Binary Representation to One

**Description:**

Given the binary representation of an integer as a string `s`, return the number of steps to reduce it to `1` under the following rules:

- If the current number is even, you have to divide it by `2`.
- If the current number is odd, you have to add `1` to it.

It is guaranteed that you can always reach one for all test cases.

Constraints: 
- The length of the given string will be between 1 and 500 inclusively. 
- The string will contain exclusively characters `1` and `0`. 
- `s[0] = '1'`

**Example:**
```
Input: s = "1101"
Output: 6
```

## Overview

My solution checks the last character of the given string for whether it's a `1` or a `0`. If `1`, we know that it's odd, so we're instructed to add `1` to the total. If `0`, we divide by `2`. We iterate this with a counter to find our desired output. When the string is `1`, we stop the counter.

The division by two can be represented by a right-shift of the binary number. This is what we opted for, in a string environment.

Adding one to the binary was a matter of flipping ones from the right until we happen upon a zero, or come to the beginning of the string.

## Reflections

Replacement of a character in a string in Python is NOT `s[2] = "0"`. I'm surprised about that. Am I picking that up from C++? We settled on `s = s[:currentDigit] + "0" + s[currentDigit+1:]`.

My solution for division by two does a split action on the string with `s[:lastPos]`. A simpler version I saw was `s.pop()`. Perfect.

Looking at other solutions to this question, I saw some conversions of the string to integer to do the calculations as an integer. `n = int(s,2)` This solution avoids any observation of the binary logic and string manipulation. Because the requirement of the problem doesn't call for string output, this may be seen as a more optimal solution.
- These solutions tend to be 8-12 lines long compared to my 35.
- These cases avoid multiple functions, less variables, less string handling, and avoid the iteration of the string logic that I did.

## Test Cases

**Case 1:** No solution. 13 in binary.
```
Input: "1101"
Output: 6
```

**Case 2:** Simple case. 2 in binary.
```
Input: "10"
Output: 1
```

**Case 3:** This is immediate success condition.
```
Input: "1"
Output: 0
```

**Case 4:** All ones. 15 in binary.
```
Input: "1111"
Output: 5
```

**Case 5:** All ones, with zero at end. 14 in binary.
```
Input: "1110"
Output: 5
```

**Case 6:** Larger case. All ones, with a zero sandwiched in. 47 in binary.
```
Input: "101111"
Output: 8
```
