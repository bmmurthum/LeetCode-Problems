class MinStack:
    
    def __init__(self):
        self.hasValue = False
        self.minValue = 0
        self.minValueIndex = 0
        self.pt = -1
        self.Stack = []
        self.minIndexList = []

    # Adds one item to the stack
    def push(self, val: int) -> None:
        if self.hasValue == False:
            self.hasValue = True
            self.Stack.append(val)
            self.minIndexList.append(0)
            self.pt = 0
            self.minimumValue = val
            self.minValueIndex = 0
        else:
            if val >= self.minimumValue:
                self.pt += 1
                self.Stack.append(val)
                self.minIndexList.append(self.minValueIndex)
            else:
                self.pt += 1
                self.Stack.append(val)
                self.minIndexList.append(self.minValueIndex)
                self.minValueIndex = self.pt
                self.minimumValue = val

    # Removes last item from the stack
    def pop(self) -> None:
        if self.Stack[self.pt] > self.minimumValue:
            del self.Stack[self.pt]
            del self.minIndexList[self.pt]
            self.pt = self.pt - 1
            if self.pt == -1:
                self.hasValue = False
        elif self.Stack[self.pt] == self.minimumValue:
            self.minimumValue = self.Stack[self.minIndexList[self.pt]]
            self.minValueIndex = self.minIndexList[self.pt]
            del self.Stack[self.pt]
            del self.minIndexList[self.pt]
            self.pt = self.pt - 1
            if self.pt == -1:
                self.hasValue = False

    # Returns the last value in the stack
    def top(self) -> int:
        return self.Stack[self.pt]

    # Returns minimum value in the stack
    def getMin(self) -> int:
        return self.minimumValue