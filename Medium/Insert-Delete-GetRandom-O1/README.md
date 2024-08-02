# Insert Delete GetRandom O(1)

**Description:**

Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average `O(1)` time complexity.

**Constraints:**

- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be at least one element in the data structure when `getRandom` is called.

## Overview

This is pretty straightforward. The exercise here is a reading exercise and a brief run of implementing a class as directed.

```python
import random
class RandomizedSet:
    """Class given by LeetCode. Implement."""

    def __init__(self):
        self.held_values = set()

    def insert(self, val: int) -> bool:
        """Inserts an element to the set."""
        if val in self.held_values:
            return False
        else:
            self.held_values.add(val)
            return True

    def remove(self, val: int) -> bool:
        """Removes an element from the set if inside."""
        if val in self.held_values:
            self.held_values.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """Return a random value from the set."""
        return random.choice(list(self.held_values))

```

## Tests

### Unit Testing

We implemented only one unit-test for this problem with `import unittest`. Simply LeetCode's given example case, which should do full code coverage.

```text
** Unit Tests **

Unit Tests Ran: 1
Methods Tested: 2
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 100% code coverage of all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
call_tests.py                        13      0   100%
insert_delete_getrandom_o1.py        16      0   100%
insert_delete_getrandom_o1_2.py      26      0   100%
memory_tests.py                      51      0   100%
time_tests.py                        87      0   100%
unit_tests.py                        57      1    98%   70
---------------------------------------------------------------
TOTAL                               250      1    99%
```

`unit_tests.py` We're missing `line 70` because this is something we'd expect to not run into with correct execution. I'd exempt this from the coverage in a more full document.

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 1: LeetCode Example.
           My Solution: 3432 blocks
    Someone's Solution: 1216 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 1: LeetCode's Example.
           My Solution runtime: 8.9380e-04 sec
    Someone's Solution runtime: 1.0074e-03 sec

Testcase 2: All Inserts.
           My Solution runtime: 1.2947e-03 sec
    Someone's Solution runtime: 1.6833e-03 sec

Testcase 3: Random Heavy.
           My Solution runtime: 6.0082e-03 sec
    Someone's Solution runtime: 5.6218e-03 sec
```

## Reflections

Differences in how the methods are implemented are seen in the time tests. In a real scenario, we may have to make a decision on which is a priority to decide between these algorithms.

I also had to write my testing differently this time.

## Solution Variations

### insert_delete_getrandom_o1_2.py

Their combination of a list and a dictionary is interesting. It may add more time in processing on a `insert()` call.

On a `getRandom()` call they already have a list prepared to call on, whereas mine has to first prepare a list from a set to call the same method.

```python
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
```
