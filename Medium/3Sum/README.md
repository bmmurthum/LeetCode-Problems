# 3Sum

**Description:**

Given an array `nums` of *n* integers, are there elements a, b, c in `nums` such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. The solution set must not contain duplicate triplets.

**Example:**
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

**To Run:**

To run this program, make sure you have Python 3. This solution is written in Python 3.8.5. Navigate to the file `3Sum.py` and run with Python. The test case to run can be chosen within the program.

```C:\>python 3Sum.py```

## Overview

For the consideration that this program may handle many cases one after another, I took the handling of edge cases to be a first priority of the algorithm so that the process-heavy nested loops may be avoided. The general steps of this program are:
1. Handle edge cases 
2. Format and sort the given list of integers
3. Iterate through the list with consideration to the nature of sums and integers

The iteration has three indexes: One index **A**, goes thoroughly from beginning to the end, the other two look for a sum that would add to the value of **A**. **B** starts at the index just after the current **A** position. **C** starts at the end of the list. **B** and **C** come inward towards eachother through logic within a single loop as they find solutions where **B** + **C** = **A**.

An [earlier solution](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/3Sum/3sum_binarySearch.py) has the loops avoid duplicate outputs by having both the outer and middle loop skip checking an integer if the last integer was the same value. For the sake of efficiency in runtime, the inner-most loop only checked on positive numbers and stops iterating on (1) finding a success, or (2) going out of possible range of success.

## Reflections

In my first run at this problem, LeetCode gave me many failed executions, even as I set out my own test cases. I saw the problems in the code and answered the individual bugs. As time went on, it began to look like I should reevaluate the structure of the logic itself. One of the last checks that LeetCode gave was to give output on a larger list of 3000 integers between -100,000 and 100,000. My code using two nested-loops and an inner binary-search would return values, but the site gave an error of "Max Time Exceeded." At this moment, I looked to other solutions. I did know that my three nested loops would have potential to run into that frustration. I figured that the nature of integers would be key to the cleverness of the iterations in the algorithm.

What I found to be a [leading thought](https://leetcode.com/problems/3sum/discuss/797132/Detailed-Explanation-with-Steps-and-Code) was an algorithm that looks at the furthest out two integers, then increments inwards as finding failed solutions. This must be faster than something like an O(n^2 * log(n)) solution than I had. I took this as a moment to break from my own dig-in of a solution, doing a full pivot.

## Further Inquiry

There was a card game, "Krypto," that I was given in late elementary school in which a player draws five integer cards from a deck, then a final goal sixth card. The goal was to add, subtract, multiply, and divide, the five cards to get to the goal card.

With much more logic, this could be a solution finder for that game. Further, it could be a generator of valid cards for exercises of various difficulty.

## Test Cases

**Case 1:**
Only positive integers, one set of zeros.
```
Input: [0, 0, 0, 1, 2, 3, 4, 5]
Output: [ [0, 0, 0]]
```

**Case 2:**
Only negative integers, one zero.
```
Input: [-1, -2, -3, 0]
Output: []
```

**Case 3:**
Empty case.
```
Input: []
Output: []
```

**Case 4:**
Set of one integer.
```
Input: [-2]
Output: []
```

**Case 5:**
Set of two integers.
```
Input: [2, -3]
Output: []
```

**Case 6:**
Set of three as a success.
```
Input: [-1, 2, -1]
Output: [ [-1,-1,2] ]
```

**Case 7:**
Set of three as a failure.
```
Input: [-1, 0, 2]
Output: []
```

**Case 8:**
A larger set of zeros.
```
Input: [0, 0, 0, 0, 0, 0]
Output: [ [0,0,0] ]
```

**Case 9:**
A breadth of a sample case.
```
Input: [-1, 0, 1, -1, 2, -1, 4]
Output: [ [-1, 0, 1], [-1, -1, 2] ]
```

**Case 10:**
A larger set with no zeros in the list.
```
Input: [6, -5, -6, -1, -2, 8, -1, 4, -10, -8, -10, -2, -4, -1, -8, -2, 8,
          9, -5, -2, -8, -9, -3, -5]
Output: [ [-10, 4, 6], [-8, -1, 9], [-6, -3, 9], [-6, -2, 8], [-5, -4, 9],
          [-5, -3, 8], [-5, -1, 6], [-4, -2, 6], [-3, -1, 4], [-2, -2, 4] ] ]
```

**Case 11:**
A set of [3000 integers](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/3Sum/largeTestCase.txt) between -100,000 and 100,000. Output is [16,258 results](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/3Sum/largeTestCaseResults.txt).
```
Input: [82597,-9243,62390,83030,-97960,-26521,-61011...]
Output: [[-99927, 2246, 97681], [-99927, 12687, 87240], [-99927, 14861, 85066], .. [-1483, -1343, 2826], [-1119, -90, 1209] ]
```
