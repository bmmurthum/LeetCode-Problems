from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for item in tokens:
            if item == "+":
                stack[-2] = stack[-2] + stack[-1]
                stack.pop()
            elif item == "-":
                stack[-2] = stack[-2] - stack[-1]
                stack.pop()
            elif item == "*":
                stack[-2] = stack[-2] * stack[-1]
                stack.pop()
            elif item == "/":
                newVal = stack[-2] / stack[-1]
                if newVal < 0:
                    newVal = int(ceil(newVal))
                else:
                    newVal = int(floor(newVal))
                stack[-2] = newVal
                stack.pop()
            else:
                stack.append(int(item))
        return stack[0]