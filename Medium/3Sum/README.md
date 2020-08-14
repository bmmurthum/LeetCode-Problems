# 3Sum

**Description:**

Given an array `nums` of *n* integers, are there elements a, b, c in `nums` such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. The solution set must not contain duplicate triplets. Solution written in Python 3.8.5.

**Example:**
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

## Reflections

I was initially very happy with myself to sort the list and find the zero at the center of the list to allow for a speedier, clever, nested-loop. Doing this, I felt that it would work smoothly if I handled the edge cases before the nested loops. There ended up being both more edge cases than I anticipated, and the structure of my loops allowed for all sorts of inner weaknesses. If I were to start again, I'd look for a more elegant set of loops.

A goal was to sort and filter the list so that the program wouldn't have to loop as much, or filter the end results of any copy results.

As LeetCode gave me failed executions, I saw the problems in the code and answered the individual bugs. As time went on, it began to look like I should reevaluate the structure of the logic itself.

## Further Inquiry

There was a card game, "Krypto," that I was given in late elementary school in which a player draws five integer cards from a deck, then a final goal sixth card. The goal was to add, subtract, multiply, and divide, the five cards to get to the goal card.

With much more logic, this could be a solution finder for that game. Further, it could be a generator of valid cards for exercises of various difficulty.

## Sample Inputs

**Case 1:**
```
Input: [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
Output: [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
```

**Case 2:**
```
Input: [-2, 0, 1, 1, 2]
Output: [[-2, 0, 2], [-2, 1, 1]]
```
