from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.ord_dict = OrderedDict()
        self.cap = capacity
        self.n = 0

    def get(self, key: int) -> int:

        if key not in self.ord_dict:
            return -1

        val = self.ord_dict.pop(key)
        self.ord_dict[key] = val

        return val

    def put(self, key: int, value: int) -> None:

        if key in self.ord_dict:
            self.ord_dict.pop(key)
        else:
            if len(self.ord_dict) >= self.cap:
                self.ord_dict.popitem(last=False)

        self.ord_dict[key] = value
