class Solution:
    def calculate(self, s: str) -> int:
        # Strip all spaces from given string
        # "  1+ 2 " becomes "1+2"
        while s != s.replace(" ",""):
            s = s.replace(" ","")
        stack = []

        # Populate stack with appropriate chars and ints
        # "(1+23)" becomes ["(",1,"+",2,3,")"] 
        for char in s:
            if char == "(" or char == ")" or char == "+" or char == "-":
                stack.append(char)
            else:
                stack.append(int(char))
        
        # Group collections of integers to one integer 
        # [1,2,3,+,4] becomes [123,+,4]
        stack.append(" ")
        stackLength = len(stack)
        i = 0
        while i < stackLength:
            while isinstance(stack[i], int) and isinstance(stack[i+1], int):
                stack[i] = int(str(stack[i])+str(stack[i+1]))
                del stack[i+1]
                stackLength -= 1
            i += 1
        stack.pop()
        
        # Associate "-" correctly to integers and parentheses
        # [-,1,+,2] becomes [-1,+,2]
        j = 0
        stackLength = len(stack)
        while j < stackLength:
            if stack[j] == "-" and j == 0 and stack[j+1] == "(":
                stack[j] = -1
                stack.insert(j+1,"*")
                stackLength += 1
                j += 1
                continue
            if stack[j] == "-" and stack[j-1] == "(" and stack[j+1] == "(":
                stack[j] = -1
                stack.insert(j+1,"*")
                stackLength += 1
                j += 1
                continue
            if stack[j] == "-" and j == 0 and isinstance(stack[j+1], int):
                stack[j] = stack[j+1] * -1
                del stack[j+1]
                stackLength -= 1
                j += 1
                continue
            if stack[j] == "-" and stack[j-1] == "(" and isinstance(stack[j+1], int):
                stack[j] = stack[j+1] * -1
                del stack[j+1]
                stackLength -= 1
                j += 1
                continue
            j += 1

        # Handling parentheses math ordering
        k = 0
        stackLength = len(stack)
        newStack = []
        lastOpenParenthesis = -1
        lastOpenList = []
        while k < stackLength:
            if stack[k] == ")":
                newStack.append(stack[k])
                lastOpenList.append(lastOpenParenthesis)

                m = lastOpenParenthesis+1
                while True:
                    if isinstance(newStack[m], int):
                        m += 1
                    elif newStack[m] == "+":
                        newStack[m-1] = newStack[m-1] + newStack[m+1]
                        del newStack[m]
                        del newStack[m]
                        lastOpenList.pop()
                        lastOpenList.pop()
                    elif newStack[m] == "-":
                        newStack[m-1] = newStack[m-1] - newStack[m+1]
                        del newStack[m]
                        del newStack[m]
                        lastOpenList.pop()
                        lastOpenList.pop()
                    elif newStack[m] == ")":
                        m = m-2
                        newStack[m] = newStack[m+1]
                        newStack.pop()
                        newStack.pop()
                        lastOpenList.pop()
                        lastOpenList.pop()
                        if len(newStack) >= 3:
                            if newStack[m-1] == "*" and newStack[m-2] == -1:
                                newStack[m-2] = newStack[m] * -1
                                newStack.pop()
                                newStack.pop()
                                lastOpenList.pop()
                                lastOpenList.pop()
                        if len(lastOpenList) > 2:
                            lastOpenList[-1] = lastOpenList[-2]
                            lastOpenParenthesis = lastOpenList[-1]
                        break
                k += 1
            else:
                newStack.append(stack[k])
                if stack[k] == "(":
                    lastOpenParenthesis = len(newStack)-1
                lastOpenList.append(lastOpenParenthesis)
                k += 1

        # Do addition subtraction after removal of parentheses
        total = newStack[0]
        i = 1
        while i < len(newStack):
            if newStack[i] == "+":
                total = total + newStack[i+1]
                i += 2
            elif newStack[i] == "-":
                total = total - newStack[i+1]
                i += 2
        return total