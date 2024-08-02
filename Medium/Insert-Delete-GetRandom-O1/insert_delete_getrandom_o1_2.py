import random


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.values.append(val)
        self.index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        index = self.index[val]
        if index == len(self.values) - 1:
            self.index.pop(val)
            self.values.pop()
        else:
            last = self.values[-1]
            self.index[last] = index
            self.values[index] = last
            self.index.pop(val)
            self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
