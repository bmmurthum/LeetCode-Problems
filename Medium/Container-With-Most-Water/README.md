# Container With Most Water

**Description:**

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

There is contraints on the inputs. The given list will have between 2 and 100,000 elements. The values of the inputs will be inclusively between 0 and 10,000.

**Example:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

## Overview

My solution sets pointers at the edges of the list, as left and right. With the height values of these two items, we calculate the volume these heights would hold given the distance between them. If this volume is larger than the current maximum of held volume, we hold that value.

We choose the pointer with the lower value to increment inward towards the other pointer.

We iterate this until we've calculated values with the two pointers one index away from another. We'll have calculated the volume n-1 times for a list of length n.

Because there is no given order to the given lists in the testing suite, we must touch the values of each item in the list at least once.

## Reflections

For as simple as this was, I was looking for small ideas of optimization. Could we hold less variables in memory? Do simpler calculations? Certainly do the least amount of looping on the list. I imagine a math library for finding a max-value of the left and right might have optimization.

I thought for a moment that you could use a consideration of the logic of the problem to skip over unusable values. Ex: If you have a currently held max-volume, iterating inward the heights of the new pointer must be larger than the old because of the shortening distance. But because the calculation of the "volume" is simple algebra on strictly necessary variables, additional if-statements and held variables seem to be unnessecary calls to memory in an iterative environment.

## Test Cases

**Case 1:** Simple case.
```
Input: [1,2,1,1,2]
Output: 6 
```

**Case 2:** With some zeroes in padding.
```
Input: [0,0,0,1,0,2,0,0,0,2]
Output: 8
```

**Case 3:** Solution in middle, neighbors.
```
Input: [0,0,0,1,0,2,10,10,0,2]
Output: 10
```

**Case 4:** Zero case. Edge case.
```
Input: [0,0]
Output: 0
```

**Case 5:** Zero case. Alternative edge case.
```
Input: [0,100]
Output: 0
```

**Case 6:** Immediate solution.
```
Input: [1,1]
Output: 1
```

**Case 7:** No solution after immediate first calculation.
```
Input: [1,1,1,1,1,1]
Output: 5
```
