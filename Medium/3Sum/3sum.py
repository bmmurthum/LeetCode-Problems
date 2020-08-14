# Brendon Murthum. August 2020.
#
# Python 3
# Leetcode Problem - 3Sum
# https://leetcode.com/problems/3sum/
#
# GOAL: Given an array nums of n integers, are there elements a, b, c in nums
#   such that a + b + c = 0? Find all unique triplets in the array which gives
#   the sum of zero.
#

# Variety of test cases.
test1 = [-1, 0, 1, -1, 2, -1, 4]
test2 = [-1, -3, -2, -1, -1, -2, -5, -10, 0, 1, 2, 3, 5, 5, 6, 7, 8, 9]
test3 = [0, 0, 0, 1, 2, 3, 4, 5]
test4 = [-1, -2, -3, 0,]
test5 = []
test6 = [-1, 0, 1]
test7 = [0, 0, 0, 0]
test8 = [-1, 0, 1, 0]
test9 = [-2, 0, 1, 1, 2]
test10 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6] # Has duplicate
testList = test10

from typing import List

# Returns a list of three-part lists, where the inner lists are three integers
# that add up to a sum of zero.
def threeSum(nums: List[int]) -> List[List[int]]:
    tempNums = []
    newNums = []

    print("Original List: ", nums)

    # Edge case of no list.
    if nums == []:
        return newNums
    # Edge case of [0,0,0]
    if nums.count(0) >= 3:
        print("More than three zeros.")
        newNums.append([0,0,0])

    # For any case of three of an integer, remove one.
    # There are no cases of three equal integers summing to 0, besides 0.
    for item in nums:
        if nums.count(item) == 3:
            nums.remove(item)
    # There are no possible cases of two zeros and another integer summing to 0.
    while (nums.count(0) > 1):
        nums.remove(0)
    # Sort, then find positive half of the list.
    nums.sort()
    posIndex = 0
    for iter in range(len(nums)):
        if nums[iter] >= 0:
            posIndex = iter
            break

    # Edge case of only three numbers.
    if len(nums) == 3:
        print("Only three numbers.")
        if nums[0] + nums[1] + nums[2] == 0:
            newNums.append([nums[0],nums[1],nums[2]])
            return newNums

    print("Editted List: ", nums)
    print("Zero: ", posIndex)

    # If there are no negative numbers, there are no cases.
    if nums[0] > 0:
        print("No negatives.")
        return newNums
    # If there are no positive numbers, there are no cases.
    if nums[len(nums) - 1] <= 0:
        print("No positives.")
        return newNums

    # The first number will be determined to be negative.
    lastB = None
    for currentIndex in range(0, posIndex):
        print("A:", nums[currentIndex])
        for b in range(currentIndex + 1, len(nums)):
            print("B:", nums[b])
            # If the same b-value as before, skip.
            if nums[b] == lastB:
                continue
            # If A and B sum to a negative.
            if nums[currentIndex] + nums[b] < 0:
                start = posIndex + 1
                # Have C-index always be after B-index.
                if nums[b] > 0:
                    start = b + 1
                for c in range(start, len(nums)):
                    print("C:", nums[c])
                    if nums[currentIndex] + nums[b] + nums[c] == 0:
                        print("Combo: ", nums[currentIndex], " + ", nums[b], " + ", nums[c])
                        tempNums = [nums[currentIndex], nums[b], nums[c]]
                        newNums.append(tempNums)
                        tempNums = []
                        break
            if nums[currentIndex] + nums[b] >= 0:
                break
            lastB = nums[b]
    return newNums

print("Result: ", threeSum(testList))
