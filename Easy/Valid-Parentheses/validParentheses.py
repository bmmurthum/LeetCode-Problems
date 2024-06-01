from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # If string-case is impossible, end now.
        if (len(s) < 2) or (len(s) % 2 == 1):
            return False
        stack = deque()
        stack.append(s[0])
        stackEndPt = 0
        for i in range(1,len(s)):
            # Add open brackets to stack
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
                stackEndPt += 1
            # If closing bracket, check for match and then pop.
            elif s[i] == ")":
                if stackEndPt < 0:
                    return False
                if stack[stackEndPt] == "(":
                    stack.pop()
                    stackEndPt -= 1
                else:
                    return False
            elif s[i] == "]":
                if stackEndPt < 0:
                    return False
                if stack[stackEndPt] == "[":
                    stack.pop()
                    stackEndPt -= 1
                else:
                    return False
            elif s[i] == "}":
                if stackEndPt < 0:
                    return False
                if stack[stackEndPt] == "{":
                    stack.pop()
                    stackEndPt -= 1
                else:
                    return False
        # If anything left on the stack after manipulation, return false.
        if len(stack) > 0:
            return False
        else:
            return True