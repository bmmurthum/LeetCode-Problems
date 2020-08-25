# Brendon Murthum. August 2020.
#
# Python 3
# Leetcode Problem - Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
#
# GOAL: Given n non-negative integers representing an elevation map where the
#   width of each bar is 1, compute how much water it is able to trap after
#   raining.
#
# OVERVIEW: My solution means to sweep from the left finding water as possible,
#   then finding the max value and most-right next-max values within the list.
#   This allows for a sweep from the right going up to that next-max value,
#   which should be a scan over the entire map. This plan means to only iterate
#   through the list four times total, (1) as from the left, (2) as sweeping
#   as finding water values backward, (3) as from the right, then (4) as
#   finding water values again.
# Lots of testing here. I made sure to draw out a variety of odd cases and find
#   their solution so that the testing function can perform well.


# Allows for use of lists.
from typing import List
# Allows for Math.floor() used in the test function.
import math


# Variety of test cases.
testCases = [
    [[0,1,0,2,1,0,1,3,2,1,2,1], 6],     # LeetCode given example
    [[2,0,0,2], 4],                     # Simple bowl
    [[4,1,1,4], 6],                     # Simple bowl
    [[0,1,0,0,1], 2],                   # Outside bowl doesn't hold anything
    [[2,3], 0],                         # Two-wide cannot hold anything
    [[1,1,1], 0],                       # Flat surface
    [[1,0,0,3,0,0,1,2,1,0,2], 10],      # Various peaks and valleys
    [[3,1,5,2,1,3,1,0,1,0,4], 22],
    [[3,0,0,3,0,2], 8],
    [[4,3,0,1,2,3,0,3,3], 9],
    [[1,0,3,1,0,1,2,1,0,2,0,1], 9],
    [[1,0,4,4,0,4,0,0,0,1,0,2,0,1], 15],
    [[2,0,4,4,0,4,0,0,1,0,2,3,1,0,2,0,1], 22],
    [[0,1,0,1,0,1,0,1,0,1,0,1], 5],
    [[0,1,0,2,0,1,0,2,0,1,0,1,0,1], 9],
    [[0,0,0,0,0,0,1,0,0,0,0,0,0,1], 6],
    [[1,0,0,0,0,0,0,0,1,0,0], 7],
    [[1,0,2,0,3,0,4,0,3,0,2,0,1], 12],
    [[2,2,0,0,1,0,2,2,3], 7],
    [[4,0,3,0,2,2,0,3,0,4], 22],
    [[4,0,3,0,2,0,5,0,2,0,3,0,4], 30],
    [[2,0,1,3,0,2,2,0,4,0,3,2,0,2,3,0,1,0,1,0,5,0,3,2,2,3,0,1,0,1,0,0,0,0,0,1,0,
        ], 55],
]


# Finds the amount of water trapped in an elevation map.
def trap(height: List[int]) -> int:

    # Handle edge-case of 0, 1, or 2 long list.
    if len(height) < 3:
        return 0

    # How much liquid is currently known to be held.
    liquidHeld = 0

    # Iterate right, finding max values, filling known value as going.
    currentMaxIndex = 0
    currentMaxValue = 0
    nextMaxIndex = 0
    nextMaxValue = 0
    hasDropped = False
    currentIndex = 0
    listLength = len(height)
    while currentIndex < listLength:
        # Handle the current max and finding liquid
        if height[currentIndex] >= currentMaxValue and hasDropped == False:
            currentMaxIndex = currentIndex
            currentMaxValue = height[currentIndex]
            nextMaxIndex = currentIndex + 1
            nextMaxValue = 0
        elif  height[currentIndex] >= currentMaxValue and hasDropped == True:
            liquidHeld += min(height[currentIndex], currentMaxValue) * (currentIndex - currentMaxIndex - 1)
            # Substract the height of values between.
            for x in range(currentMaxIndex + 1, currentIndex):
                liquidHeld -= height[x]
            hasDropped = False
            currentMaxIndex = currentIndex
            currentMaxValue = height[currentIndex]
            nextMaxIndex = currentIndex + 1
            nextMaxValue = 0
        elif height[currentIndex] < currentMaxValue:
            hasDropped = True
        # Finding the next highest value for the iteration backward later.
        if height[currentIndex] >= nextMaxValue and \
           height[currentIndex] < currentMaxValue:
            nextMaxIndex = currentIndex
            nextMaxValue = height[currentIndex]
        # Increment Current Index
        currentIndex += 1

    # Handling a overstepping-bounds issue.
    if nextMaxIndex >= listLength:
        nextMaxIndex = listLength - 1

    # Add liquid from max to right-most max.
    if nextMaxValue < currentMaxValue and nextMaxValue != 0:
        liquidHeld += min(height[currentMaxIndex], height[nextMaxIndex]) * (nextMaxIndex - currentMaxIndex - 1)
        for x in range(currentMaxIndex + 1, nextMaxIndex):
            liquidHeld -= height[x]

    # Iterate left to the right-most max value, filling as going.
    currentMaxIndex = len(height) - 1
    currentIndex = len(height) - 1
    currentMaxValue = 0
    hasDropped = False
    while currentIndex >= nextMaxIndex:
        if height[currentIndex] >= currentMaxValue and hasDropped == False:
            currentMaxIndex = currentIndex
            currentMaxValue = height[currentIndex]
        elif  height[currentIndex] >= currentMaxValue and hasDropped == True:
            liquidHeld += min(height[currentIndex], currentMaxValue) * (currentMaxIndex - currentIndex - 1)
            # Substract the height of values between.
            for x in range(currentIndex + 1, currentMaxIndex):
                liquidHeld -= height[x]
            hasDropped = False
            currentMaxIndex = currentIndex
            currentMaxValue = height[currentIndex]
        elif height[currentIndex] < currentMaxValue:
            hasDropped = True
        # Decrement Current Index
        currentIndex -= 1

    return liquidHeld


# Runs the function through test values.
def testFunction(testList):
    numberOfTests = len(testList)
    numberOfSuccesses = 0
    for test in testList:
        if trap(test[0]) != test[1]:
            print("FAILURE:", test[0], "!= " + str(trap(test[0])) + ",",
                  "should be: " + str(test[1]))
            None
        else:
            # print("SUCCESS:", test[0], "== " + str(trap(test[0])))
            numberOfSuccesses += 1
    percentSuccess = math.floor((numberOfSuccesses / numberOfTests) * 100)
    print(str(percentSuccess) + "% Success " + str(numberOfSuccesses) + \
          "/" + str(numberOfTests) + " Cases")


# Run the test function.
testFunction(testCases)
