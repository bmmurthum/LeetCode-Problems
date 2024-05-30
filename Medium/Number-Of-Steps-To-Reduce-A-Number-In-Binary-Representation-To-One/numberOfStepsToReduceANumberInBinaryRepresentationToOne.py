def numSteps(binaryString):
    if binaryString == "1":
        return 0
    stepsTaken = 0
    newNum = binaryString
    while newNum != "1":
        if newNum[len(newNum) - 1] == "1":
            newNum = plusOne(newNum)
        else:
            newNum = divideByTwo(newNum)
        stepsTaken += 1
    return stepsTaken

# Returns a string of the represented binary summed with one.
def plusOne(s):
    lastDigit = len(s) - 1
    currentDigit = lastDigit
    s = s[:currentDigit] + "0" + s[currentDigit+1:]
    currentDigit -= 1
    while True:
        if currentDigit == -1:
            s = "1" + s
            break
        if s[currentDigit] == "1":
            s = s[:currentDigit] + "0" + s[currentDigit+1:]
        else:
            s = s[:currentDigit] + "1" + s[currentDigit+1:]
            break
        currentDigit -= 1
    return s

# Returns a string of the represented binary divided by two.
def divideByTwo(s):
    x = len(s)-1
    return s[:x]

testCase_1 = "1101"   # 13 - Steps: 6
testCase_2 = "10"     # 2  - Steps: 1
testCase_3 = "1"      # 1  - Steps: 0
testCase_4 = "1111"   # 15 - Steps: 5
testCase_5 = "1110"   # 14 - Steps: 5
testCase_6 = "101111" # 47 - Steps: 8

print(numSteps(testCase_6))