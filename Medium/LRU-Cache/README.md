# LRU Cache

**Description:**

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity.
- `int get(int key)` Return the value of the key if the key exists, otherwise return -1.
- `void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions `get` and `put` must each run in O(1) average time complexity.

```python
class LRUCache:
    def __init__(self, capacity: int):
        # ...
    def get(self, key: int) -> int:
        # ...
    def put(self, key: int, value: int) -> None:
        # ...

# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

**Example:**

```text
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
```

## Overview

For my [solution](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/LRU-Cache/lru_cache.py) we have a `hash_table` with attached linked-linked lists at each index. Each `ListNode` holds values for the pointer to the next item in the hash-table as well as its neighbors in the LRU linked-list.

For any given `put()` or `get()` we update the hash-table and LRU list. Any `put()` that would get us above capacity calls us to remove the `head_ptr` from the LRU list, after adding a value at the `tail_ptr`.

Our `_hash` function is called on the `key` integer of the request to find the index that this `ListNode` would be stored at. We set up the `_hash` to have an option for having the number of indexes in the hash-table to be larger than necessary to minimize lengths of linked chains if desired. We can change `multiplier_hash_table` from `1` to `2` for a twice-large as necessary table, using more memory, but lessening the chain lengths for less calls to memory.

```python
#   Hash Table
#   0 : Node(A) -> Node(C)
#   1 : Node(B)
#   2 :
#   3 : Node(D)
# A.hash_next == C
# hash_table[0] == A
# hash_table[2] == None

#   LRU Linked-List
#   A > B > C > D
#   H           T
# A.next == B
# C.prev == B
# D.next == None
# head_ptr == A
# tail_ptr == D
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and straining the range of values written in constraints. We checked for:

- Large list of inputs and checks
- Our retrieved value deeper within linked-list in hash-table
- Updating the only item stored

### Code Coverage

We received 100% code coverage on each tested method from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run unit_test.py
> coverage report -m 
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
lru_cache.py       107      0   100%
lru_cache_2.py      18      0   100%
test_cases.py       10      0   100%
unit_test.py        48      0   100%
----------------------------------------------
TOTAL              183      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution and someone else's on a 100-item case. My solution uses almost twice the memory.

Memory blocks used:

- `My solution`: 3680 blocks
- `Other solution`: 2248 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on the same input. My solution is 3x slower.

- `My solution`: 6.015 x 10^-5 sec
- `Other solution`: 2.054 x 10^-5 sec

## Reflections

This problem prompted me to write up a new way to test inputs. I'm now putting my test-inputs with their solutions into a new file to import into my tests.

With all of the pointers and node traversals, the bug-hunting was an exercise in setting breakpoints and stepping through.

## Solution Variations

This solution, written by someone else, uses Python's `OrderedDict` library. It seems that this native library performs the functions by design. It's being-ordered by key allows for a `pop()` in the order of least-recently-used.

It doesn't exercise linked-list manipulation or hash-tables as from the prompt, but is notably more efficient. This is likely related to it's using C from the Python modules.

```python
# Someone else's solution
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
```
