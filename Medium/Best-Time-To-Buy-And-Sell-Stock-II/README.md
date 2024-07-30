# Best Time to Buy and Sell Stock II

**Description:**

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

**Constraints:**

- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

**Examples:**

```text
Input: prices = [7,1,5,3,6,4]
Output: 7

Input: prices = [1,2,3,4,5]
Output: 4

Input: prices = [7,6,4,3,1]
Output: 0
```

## Overview

My solution, with its seeing into the future, buys on lows and sells on highs essentially. It sets the `bought` to the lowest its seen, and "sells" when the next value is lower than the current value.

```python
class Solution:
    """Problem given by LeetCode."""

    def max_profit(self, prices: list[int]) -> int:
        """
        Looks for a best profit to be made with multiple buys and sell on a
        list of known prices.

        Args:
            `prices`: A list of prices of a stock.
        Returns:
            `max_profit`: The best profit return that can be found.
        """

        # Handle single item list case
        if len(prices) == 1:
            return 0

        # When the next one is higher, grab this
        # When the next one is lower, sell this
        bought = float("inf")
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1] and prices[i] < bought:
                bought = prices[i]
            elif prices[i] > prices[i + 1] and bought != float("inf"):
                profit += prices[i] - bought
                bought = float("inf")
        if bought != float("inf") and prices[-1] > bought:
            profit += prices[-1] - bought
        return profit
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's three example cases
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

We received 100% code coverage of all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
best_time_to_buy_and_sell_stocks_ii.py        15      0   100%
best_time_to_buy_and_sell_stocks_ii_2.py       7      0   100%
best_time_to_buy_and_sell_stocks_ii_3.py       9      0   100%
call_tests.py                                 13      0   100%
memory_tests.py                               84      0   100%
testcases.py                                  47      0   100%
time_tests.py                                 75      0   100%
unit_tests.py                                124      0   100%
--------------------------------------------------------------
TOTAL                                        374      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 9: 1000 items, best sell at end.
      max_profit(): 528 blocks
    max_profit_2(): 528 blocks
    max_profit_3(): 536 blocks

Testcase 10: 1000 items, best sell near beginning.
      max_profit(): 520 blocks
    max_profit_2(): 520 blocks
    max_profit_3(): 528 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 9: 1000 items, best sell at end.
      max_profit() runtime: 1.1143e-01 sec
    max_profit_2() runtime: 6.2963e-02 sec
    max_profit_3() runtime: 6.4782e-02 sec

Testcase 10: 1000 items, best sell near beginning.
      max_profit() runtime: 1.1070e-01 sec
    max_profit_2() runtime: 6.2473e-02 sec
    max_profit_3() runtime: 6.5247e-02 sec
```

## Reflections

I thought there may be some time benefit in only selling when I'd need to. This ends up not being true. My solution does less interactions with the total profit variable than the other solutions, at the cost of more calls for comparisons.

## Solution Variations

### best_time_to_buy_and_sell_stock_ii_2.py

"If tomorrow's price is higher, sell it tomorrow."

```python
class Solution:
    def max_profit_2(self, prices: list[int]) -> int:
        running_profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] > prices[i]:
                running_profit += prices[i + 1] - prices[i]
        return running_profit
```

### best_time_to_buy_and_sell_stock_ii_3.py

"If yesterday's price was lower, sell it today."

```python
class Solution:
    def max_profit_3(self, prices: list[int]) -> int:
        max_profit = 0
        current_buy_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > current_buy_price:
                max_profit += prices[i] - current_buy_price
            current_buy_price = prices[i]
        return max_profit
```
