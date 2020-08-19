# Brendon Murthum. August 2020.
#
# Python 3
# Leetcode Problem - Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
#
# GOAL: Roman numerals are represented by seven different symbols: I, V, X, L,
#   C, D and M. For example, two is written as II in Roman numeral, just two
#   one's added together. Twelve is written as, XII, which is simply X + II.
#   The number twenty seven is written as XXVII, which is XX + V + II.
#   Roman numerals are usually written largest to smallest from left to right.
#   However, the numeral for four is not IIII. Instead, the number four is
#   written as IV. Because the one is before the five we subtract it making
#   four. The same principle applies to the number nine, which is written as
#   IX. Given a roman numeral, convert it to an integer. Input is guaranteed
#   to be within the range from 1 to 3999.
#
# OVERVIEW: For this program I wanted to first have a grasp on the system of
#   roman numerals to see if I could see any patterns that may be good for the
#   logic of the algorithms. I used
#   https://www.mathsisfun.com/roman-numerals.html to explore logic and
#   generate test cases.
# This problem, focused on processing a string, doesn't call for eyes to
#   parallel-processing, reducing memory usage, or reducing process time.
#   Those would be worthy efforts, but not my desire here. I aimed for a goal
#   of ease in readability and a large set of test-cases, with a partnered
#   testing function to iterate through all the test-cases.


# Allows for use of lists.
from typing import List
# Allows for Math.floor() used in the test function.
import math


# Variety of test cases.
testCases = [
    ["I", 1],               # Common Small Cases
    ["II", 2],
    ["III", 3],
    ["IV", 4],
    ["V", 5],
    ["VI", 6],
    ["VII", 7],
    ["VIII", 8],
    ["IX", 9],
    ["X", 10],
    ["XI", 11],
    ["ii", 2],              # Lower-Case Allowed
    ["xii", 12],
    ["ccxxxiii", 233],
    ["LVIII", 58],          # Leetcode Example Cases.
    ["MCMXCIV", 1994],
    ["XXIII", 23],          # Variety of Cases.
    ["XXIX", 29],
    ["XXXV", 35],
    ["XL", 40],
    ["XLII", 42],
    ["XLVIII", 48],
    ["LIV", 54],
    ["LXIV", 64],
    ["LXXIV", 74],
    ["LXXVI", 76],
    ["LXXXIX", 89],
    ["XC", 90],
    ["XCIV", 94],
    ["XCIX", 99],
    ["CXIX", 119],
    ["CLXVIII", 168],
    ["CLXXIX", 179],
    ["CCXXV", 225],
    ["CCXXIX", 229],
    ["CCXCIX", 299],
    ["CCCXLIX", 349],
    ["CCCXCIX", 399],
    ["CD", 400],
    ["CDI", 401],
    ["CDXXIII", 423],
    ["CDLXXVI", 476],
    ["CDLXXXVIII", 488],    # Ten-Character String.
    ["CDXCIX", 499],
    ["D", 500],
    ["CMXCIX", 999],
    ["M", 1000],            # Above 1,000.
    ["MVIII", 1008],
    ["MIX", 1009],
    ["MXLIX", 1049],
    ["MXCIX", 1099],
    ["MCCCXXXVII", 1337],
    ["MCMXCIX", 1999],      # Three Cases of Subtraction.
    ["MMXLIX", 2049],
    ["MMLXVIII", 2068],
    ["MMDLXXVI", 2576],
    ["MMDCXCIX", 2699],
    ["MMCMXCIX", 2999],
    ["MMML", 3050],
    ["MMMLXXIX", 3079],
    ["MMMCDLV", 3455],
    ["MMMDLXVI", 3566],
    ["MMMCMXCVIII", 3998],
    ["MMMCMXCIX", 3999],    # Highest Case to Test For.
    ["MMMM", 4000]
]


# This function takes a string of a roman numeral and returns a valid integer.
def romanToInt(s: str) -> int:

    # A list of the initial letters as their represented numbers.
    numberList = []

    # Convert the letters in the string to a list of numbers.
    # For ease of working with logic.
    for letter in s:
        letter = letter.upper()
        if letter == "I":
            numberList.append(1)
        elif letter == "V":
            numberList.append(5)
        elif letter == "X":
            numberList.append(10)
        elif letter == "L":
            numberList.append(50)
        elif letter == "C":
            numberList.append(100)
        elif letter == "D":
            numberList.append(500)
        elif letter == "M":
            numberList.append(1000)

    # Process the list.
    sum = 0
    currentIndex = 0
    length = len(numberList)
    while True:
        # If done iterating, exit.
        if currentIndex >= length:
            break

        # If at last value in the list.
        if currentIndex == length - 1:
            sum += numberList[currentIndex]
            break

        # Set iterating values.
        currentValue = numberList[currentIndex]
        nextValue = numberList[currentIndex + 1]

        # Unique cases of substraction.
        if currentValue == 1 and nextValue == 5:
            sum += 4
            currentIndex += 2
        elif currentValue == 1 and nextValue == 10:
            sum += 9
            currentIndex += 2
        elif currentValue == 10 and nextValue == 50:
            sum += 40
            currentIndex += 2
        elif currentValue == 10 and nextValue == 100:
            sum += 90
            currentIndex += 2
        elif currentValue == 100 and nextValue == 500:
            sum += 400
            currentIndex += 2
        elif currentValue == 100 and nextValue == 1000:
            sum += 900
            currentIndex += 2
        # All other cases are simple addition to the total.
        else:
            sum += currentValue
            currentIndex += 1
    # Return the total.
    return sum


# Runs the function through test values.
def testFunction(testList):
    numberOfTests = len(testList)
    numberOfSuccesses = 0
    for test in testList:
        if romanToInt(test[0]) != test[1]:
            print("FAILURE:", test[0], "!= " + str(romanToInt(test[0])) + ",",
                  "should be: " + str(test[1]))
            None
        else:
            numberOfSuccesses += 1
    percentSuccess = math.floor((numberOfSuccesses / numberOfTests) * 100)
    print(str(percentSuccess) + "% Success " + str(numberOfSuccesses) + \
          "/" + str(numberOfTests) + " Cases")


# Run the test function.
testFunction(testCases)
