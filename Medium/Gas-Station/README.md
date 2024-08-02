# Gas Station

**Description:**

There are `n` gas stations along a circular route, where the amount of gas at the `ith` station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `ith` station to its next `(i + 1)th` station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is guaranteed to be unique.

**Constraints:**

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

**Examples:**

```text
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
```

## Overview

For my solution, first we can rule-out a negative case by comparing the list sums. Then knowing there is a solution, we can look at each station to see "if we started here, would we run out of gas?"

```python
class Solution:
    """Problem by LeetCode.com"""

    def can_complete_circuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Find the gas station that will allow us to do a complete circuit.
        Returns `-1` if none are good.

        Args:
            `gas`: The amount of gas at a station.
            `cost`: The amount of gas to get to the next station.
        Returns:
            `possible_start`: The index of the station to start at.
        """

        # If the total gas is less than cost, there is no solution.
        if sum(gas) - sum(cost) < 0:
            return -1

        # For each station, "Have we run out of gas?"
        # "What if we started at the next one?"
        total_gas = 0
        possible_start = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            if total_gas < 0:
                total_gas = 0
                possible_start = i + 1
        return possible_start
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's two example cases.
- Lots of gas at the last station.
- Gas found in front several stations.
- Gas found in last stations.
- Start position of last index.
- Variations of 1000-long cases.

```text
** Unit Tests **

Unit Tests Ran: 11
Methods Tested: 4
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 99% code coverage of all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
call_tests.py         13      0   100%
gas_station.py        12      0   100%
gas_station_2.py      12      0   100%
gas_station_3.py      23      1    96%   24
gas_station_4.py      12      0   100%
memory_tests.py      217      0   100%
testcases.py          82      0   100%
time_tests.py         53      1    98%   112
unit_tests.py        156      0   100%
------------------------------------------------
TOTAL                580      2    99%
```

On the missing `line 24` in `gas_station_3.py`: This is a line that'll never be reached.

`time_tests.py` coverage can be ignored.

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Case 8: 1000 Long. Front loaded.
      can_complete_circuit(): 596 blocks
    can_complete_circuit_2(): 596 blocks
    can_complete_circuit_3(): 9808 blocks
    can_complete_circuit_4(): 14023 blocks

Case 9: 1000 Long. Back loaded.
    can_complete_circuit_2(): 592 blocks
      can_complete_circuit(): 8224 blocks
    can_complete_circuit_3(): 9800 blocks
    can_complete_circuit_4(): 18094 blocks

Case 10: 1000 Long. Starts at back index.
      can_complete_circuit(): 580 blocks
    can_complete_circuit_2(): 580 blocks
    can_complete_circuit_3(): 9792 blocks
    can_complete_circuit_4(): 18086 blocks

Case 11: 1000 Long. No valid start.
    can_complete_circuit_2(): 488 blocks
      can_complete_circuit(): 504 blocks
    can_complete_circuit_3(): 17136 blocks
    can_complete_circuit_4(): 34262 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Case 8: 1000 Long. Front loaded.
    can_complete_circuit_4() runtime: 3.008 x (10 ^ -2) sec
      can_complete_circuit() runtime: 8.145 x (10 ^ -2) sec
    can_complete_circuit_2() runtime: 9.265 x (10 ^ -2) sec
    can_complete_circuit_3() runtime: 2.176 x (10 ^ -1) sec

Case 9: 1000 Long. Back loaded.
    can_complete_circuit_4() runtime: 3.324 x (10 ^ -2) sec
    can_complete_circuit_2() runtime: 8.675 x (10 ^ -2) sec
      can_complete_circuit() runtime: 9.799 x (10 ^ -2) sec
    can_complete_circuit_3() runtime: 3.062 x (10 ^ -1) sec

Case 10: 1000 Long. Starts at back index.
    can_complete_circuit_4() runtime: 3.411 x (10 ^ -2) sec
      can_complete_circuit() runtime: 8.323 x (10 ^ -2) sec
    can_complete_circuit_2() runtime: 9.274 x (10 ^ -2) sec
    can_complete_circuit_3() runtime: 3.874 x (10 ^ -1) sec

Case 11: 1000 Long. No valid start.
      can_complete_circuit() runtime: 4.678 x (10 ^ -3) sec
    can_complete_circuit_2() runtime: 4.733 x (10 ^ -3) sec
    can_complete_circuit_4() runtime: 6.026 x (10 ^ -2) sec
    can_complete_circuit_3() runtime: 1.043 x (10 ^ -1) sec
```

## Reflections

I spend time on this problem updating the time tests to be easier to copy-paste between problems.

## Solution Variations

### gas_station_2.py

The same as mine, but assigning variables differently.

```python
class Solution:
    def can_complete_circuit_2(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        cur_gas, ans = 0, 0
        for i in range(len(cost)):
            if cur_gas < 0:
                ans = i
                cur_gas = gas[i] - cost[i]
            else:
                cur_gas += gas[i]
                cur_gas -= cost[i]
        return ans
```

### gas_station_3.py

They have some unused variables. It looks like they intentionally made this obfuscated with no variable names.

```python
class Solution:
    def can_complete_circuit_3(self, gas: list[int], cost: list[int]) -> int:
        c = 0
        d = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(d) < 0:
            return -1
        if len(d) == 1:
            return 0
        i = 0
        k = 0
        t = 0
        j = 0
        while i < len(d):
            k = k + d[j]
            t = j
            j = (j + 1) % len(d)
            if k < 0:
                k = 0
                i = -1
            i += 1
        if k >= 0:
            return j
        else:
            return -1
```

### gas_station_4.py

Using Numpy arrays, how fun. Does the use of classically styled arrays play for a better read efficiency here?

```python
import numpy as np
class Solution:
    def can_complete_circuit_4(self, gas: list[int], cost: list[int]) -> int:
        diff = np.array(gas) - np.array(cost)
        i = 0
        while i < len(diff):
            con = np.concatenate([diff[i:], diff[:i]])
            cum_sum = np.cumsum(con)
            if cum_sum.min() >= 0:
                return i
            i = cum_sum.argmin() + 1 + i
        return -1
```
