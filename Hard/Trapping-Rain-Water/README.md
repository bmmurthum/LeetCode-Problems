# Trapping Rain Water

**Description:**

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

**Example:**
```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**To Run:**

To run this program, make sure you have Python 3. The solution is written in Python 3.8.5. Navigate to the file `trappingRainWater.py` and run with Python. Running the program as it is provided [here](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Hard/Trapping-Rain-Water/trappingRainWater.py) runs the solution algorithm through many test cases. You're welcome to add your own test cases to the initial list. Failed tests output a failure message.

`$ python trappingRainWater.py`

## Overview

My solution means to sweep from the left finding water as possible, then finding the max value and most-right next-max values within the list. This allows for a sweep from the right going up to that next-max value, which should be a scan over the entire map. This plan means to only iterate through the list in four pieces total, less than four full runs of the list.
1. From the left in totality, finding a max peak and second highest peak.
2. Sweeping backward to find water values within the first iteration.
3. From the right to the point of the second-highest peak.
4. Sweeping backward within the (3) iteration, finding water values.

There was lots of testing integrated from the beginning. I made sure to draw out a variety of odd cases on paper and find their solution so that the testing function can perform well. In the end, I drew out 22 cases to run the program through.

## Reflections

On this problem, I made sure to draw out several odd cases for ideation of a workable function. This worked a couple first thoughts out of the running. It also gave space to think about a most efficient cycle of iteration.

LeetCode reports that my program's runtime is faster than 21% of submissions, which is nothing to brag about. Looking at the graph of submissions, mine is right at the slower end of the bell curve. Nothing embarrassing.

## Further Inquiry

- Having a JavaScript version of this solution with generated displays would be very approachable for a viewer.
- Writing a program that fills a display of the water spaces would be nice. Another challenge might be "find the squares with water in them," rather than "how many water spaces."
- Further competing with the percentiles of runtime speed submissions.

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
