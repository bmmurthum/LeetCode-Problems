# Trapping Rain Water

**Description:**

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

**Example:**
```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

## Overview

My solution means to sweep from the left finding water as possible, then finding the max value and most-right next-max values within the list. This allows for a sweep from the right going up to that next-max value, which should be a scan over the entire map. This plan means to only iterate through the list four times total, (1) as from the left, (2) as sweeping as finding water values backward, (3) as from the right, then (4) as finding water values again.

There was lots of testing integrated from the beginning. I made sure to draw out a variety of odd cases on paper and find their solution so that the testing function can perform well.

## Reflections

## Further Inquiry

- Having a JavaScript version of this solution with generated displays would be very approachable for a viewer.

## Test Cases

**Case 1:** A simple bowl.
```
Input: [2,0,0,2]
Output: 4  
```

**Case 2:** A simple raised bowl.
```
Input: [4,1,1,4]
Output: 6
```

**Case 3:** Outside bowl doesn't trap water.
```
Input: [[0,1,0,0,1]
Output: 2
```

**Case 4:** A flat surface.
```
Input: [1,1,1]
Output: 0
```

**Case 5:** A two-wide setup.
```
Input: [2,3]
Output: 0
```

**Case 6:** Various setups of peaks and valleys.
```
Input: [1,0,0,3,0,0,1,2,1,0,2]
Output: 10
```

**Case 7:** Various setups of peaks and valleys.
```
Input: [3,1,5,2,1,3,1,0,1,0,4]
Output: 22
```

**Case 8:** Various setups of peaks and valleys.
```
Input: [4,3,0,1,2,3,0,3,3]
Output: 9
```

**Case 9:** Various setups of peaks and valleys.
```
Input: [1,0,4,4,0,4,0,0,0,1,0,2,0,1]
Output: 15
```

**Case 10:** Various setups of peaks and valleys.
```
Input: [2,0,4,4,0,4,0,0,1,0,2,3,1,0,2,0,1]
Output: 22
```
