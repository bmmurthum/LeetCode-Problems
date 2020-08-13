# Brendon Murthum. August 2020.
#
# Python 3
# Leetcode Problem - Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# GOAL: Given a string, find the length of the longest substring without
#   repeating characters.
#
# My approach to this was with entry Python knowledge. I put little effort to
#   optimization in terms of memory use and of O() time complexity. My aim was
#   to complete the requirements quickly with high readability.
# In a second run at this problem, I would aim to store indexes of critical
#   positions in order to avoid backward iteration. I would also aim to avoid
#   hard-coding for edge cases and initial states.

# Variety of test cases.
test1 = "abcabcbb"      # Outputs 3
test2 = "bbbbb"         # Outputs 1
test3 = "pwwkew"        # Outputs 3
test4 = "z"             # Outputs 1
test5 = ""              # Outputs 0
test6 = "ab"            # Outputs 2
testString = test1

# Returns the longest string of characters within string that do not contain
# duplicate characters.
def lengthOfLongestSubstring(s: str) -> int:

    # Initialize helper variables.
    givenString = s
    largestSubstring = ""
    largestSubstringLength = 0
    currentString = ""

    # If the given string is nothing.
    if len(givenString) == 0:
        return 0

    # Add the first letter as the longest substring.
    currentString = givenString[0]
    currentFrontIndex = 0
    largestSubstringLength = 1
    breakingCharacter = ""

    # Iterate through the given full string.
    while currentFrontIndex < len(givenString) - 1:
        currentFrontIndex += 1
        # Check the holding string for duplicate characters.
        hasDuplicate = False
        for letter in currentString:
            if givenString[currentFrontIndex] == letter:
                hasDuplicate = True
                breakingCharacter = letter
                break
        # Build the current found substring.
        if hasDuplicate == False:
            currentString = currentString + givenString[currentFrontIndex]
        # Iterate back to first copy of found duplicate letter.
        if hasDuplicate == True:
            # Go back one.
            currentFrontIndex -= 1
            # Go to last copy of character.
            while breakingCharacter != givenString[currentFrontIndex]:
                currentFrontIndex -= 1
            # Go forward one character.
            currentFrontIndex += 1
            currentString = givenString[currentFrontIndex]
        # Write to holder variabnle if current string is the largest yet.
        if len(currentString) > largestSubstringLength:
            largestSubstringLength = len(currentString)
            largestSubstring = currentString
    return largestSubstringLength;

# Output of Function
print("Largest Substring Length: ", lengthOfLongestSubstring(testString))
