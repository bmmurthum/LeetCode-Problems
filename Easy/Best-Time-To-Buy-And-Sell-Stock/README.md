# Copy List with Random Pointer

**Description:**

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

**Constraints:**

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

**Examples:**

```text
Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0
```

## Overview

My solution iterates through `prices` to look for a `price` that is now the newest seen lowest. If true, we subtract the `max()` value of the values after this one in the remaining list.

```python
class Solution:
    """Problem given by LeetCode."""

    def max_profit(self, prices: list[int]) -> int:
        """
        Looks for a best profit case between a buy and sell on known prices.

        Args:
            `prices`: A list of prices of a stock.
        Returns:
            `max_profit`: The best profit return that can be found.
        """

        # Handle edge case
        if len(prices) == 1:
            return 0

        # Look for largest difference whenever we find a new lowest-num
        temp_min = 10**4 + 1
        max_profit = 0
        for i, price in enumerate(prices[0:-1]):
            if price < temp_min:
                temp_min = price
                temp_best_profit = max(prices[i + 1 :]) - price
                if temp_best_profit > max_profit:
                    max_profit = temp_best_profit

        return max_profit
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's two example cases
- All descending numbers
- All ascending numbers
- Good match in beginning, then a better match
- Same match in beginning and end
- Minimum value at end
- Values all zeroes
- List length of 1, exercising given constraint limits

```text
** Unit Tests **

Unit Tests Ran: 10
Methods Tested: 3
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 99% code coverage of all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report -m
Name                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
best_time_to_buy_and_sell_stock.py        13      0   100%
best_time_to_buy_and_sell_stock_2.py       7      0   100%
best_time_to_buy_and_sell_stock_3.py      12      1    92%   4
call_tests.py                             13      0   100%
memory_tests.py                           84      0   100%
testcases.py                              47      0   100%
time_tests.py                             75      0   100%
unit_tests.py                            124      0   100%
--------------------------------------------------------------------
TOTAL                                    375      1    99%
```

The missing line in `best_time_to_buy_and_sell_stock_3.py` is its handle of an empty list as the given argument. The constraints of the problem insist that the input list will be at the lowest length of 1, so this is not covered by the unit tests.

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 9: 1000 items, best sell at end.
      max_profit(): 560 blocks
    max_profit_2(): 384 blocks
    max_profit_3(): 320 blocks

Testcase 10: 1000 items, best sell near beginning.
      max_profit(): 560 blocks
    max_profit_2(): 384 blocks
    max_profit_3(): 320 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 9: 1000 items, best sell at end.
      max_profit() runtime: 5.5057e-02 sec
    max_profit_2() runtime: 1.3922e-01 sec
    max_profit_3() runtime: 6.2216e-02 sec

Testcase 10: 1000 items, best sell near beginning.
      max_profit() runtime: 5.3871e-02 sec
    max_profit_2() runtime: 1.3681e-01 sec
    max_profit_3() runtime: 6.0456e-02 sec
```

## Reflections

I'd like to use lest logic on list truncation when simple logic may be cleaner and less process-time heavy.

## Solution Variations

### best_time_to_buy_and_sell_stock_2.py

This is a particular style of writing. Dense lines of code.

This method runs slowest of our three cases and I'd say is less readable.

This method works by iterating over `prices` and at each item setting their lowest-value holder `l` and their max-profit `mp` found. The inefficiency here seems to be in doing the assigning and calling of variables in each iteration.

```python
class Solution:
    def max_profit_2(self, prices: list[int]) -> int:
        l, n, mp = 0, len(prices), 0
        for i in range(1, n):
            l = i if prices[i] < prices[l] else l
            mp = max(prices[i] - prices[l], mp)
        return mp
```

### best_time_to_buy_and_sell_stock_3.py

`min_price = float("inf")`. I like this. In a similar action, I made sure to set my minimum-holder to an integer above the max allowed.

This is a cleaner version of my solution. My line of `temp_best_profit = max(prices[i + 1 :]) - price` could be replaced by looking at a comparison of `price` with `min_price`. My calling on a truncation of the initial `prices` list is likely costly in time.

```python
class Solution:
    def max_profit_3(self, prices: list[int]) -> int:
        if not prices:
            return 0

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
```
