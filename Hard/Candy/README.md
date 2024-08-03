# Candy

**Description:**

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

**Constraints:**

- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`

**Examples:**

```text
Input: ratings = [1,0,2]
Output: 5

Input: ratings = [1,2,2]
Output: 4
```

## Overview

For my solution we do the following:

1. Handle small cases and base setup.
2. Setup for iteration by building a list of `local_minimums` to start iterating at in the `ratings` list.
3. Starting at each `local_min`, we look to the left and look to the right until we come to a peak. While we do this, we're logging the candies we'd give to each child with the list `candies_to_give`.
4. When done looking from the local minimums, we'd have built a complete list of how many candies we'd give to each child. We can now return `sum(candies_to_give)`.

```python
class Solution:
    """Problem by LeetCode.com"""

    def candy(self, ratings: list[int]) -> int:
        """
        Return the minimum amount of candy to give to a group of kids. You must
        give more candy to a kid than their neighbor that has a lower rating.

        Args:
            `ratings`: The goodness rating of this child.
        Returns:
            `total_candies`: The minimum number of candies given out.
        """

        # Handle small cases
        length = len(ratings)
        if length == 1:
            return 1
        if length == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3

        # A list of candy to give to children
        candies_to_give = [-1] * length

        # Find all local minimums
        local_minimums = []
        for i in range(length):
            # Look at neighbors
            left_is_larger = False
            right_is_larger = False
            if i != 0 and ratings[i - 1] > ratings[i]:
                left_is_larger = True
            if i != length - 1 and ratings[i + 1] > ratings[i]:
                right_is_larger = True
            left_is_smaller = False
            right_is_smaller = False
            if i != 0 and ratings[i - 1] < ratings[i]:
                left_is_smaller = True
            if i != length - 1 and ratings[i + 1] < ratings[i]:
                right_is_smaller = True
            # Note as a minimum
            if (left_is_larger or right_is_larger) and not (
                left_is_smaller or right_is_smaller
            ):
                local_minimums.append(i)
                candies_to_give[i] = 1
                continue
            # If flat, note as one candy
            if not (
                left_is_larger or right_is_larger or left_is_smaller or right_is_smaller
            ):
                candies_to_give[i] = 1

        # Start iterations over the main list from various local_min.
        for local_min in local_minimums:

            # Look at neighbors
            left_is_larger = False
            right_is_larger = False
            if local_min != 0 and ratings[local_min - 1] > ratings[local_min]:
                left_is_larger = True
            if local_min != length - 1 and ratings[local_min + 1] > ratings[local_min]:
                right_is_larger = True

            # Go left from local_min
            if left_is_larger:
                last_amount = 1
                for i in range(local_min - 1, -1, -1):
                    right_is_smaller = ratings[i + 1] < ratings[i]
                    if right_is_smaller:
                        # If this spot has yet to be noted
                        if candies_to_give[i] == -1:
                            candies_to_give[i] = last_amount + 1
                        # If this spot has been seen
                        elif last_amount + 1 > candies_to_give[i]:
                            candies_to_give[i] = last_amount + 1
                            break
                        else:
                            break
                        last_amount += 1
                    else:
                        break

            # Go right from local_min
            if right_is_larger:
                last_amount = 1
                for i in range(local_min + 1, length):
                    left_is_smaller = ratings[i - 1] < ratings[i]
                    if left_is_smaller:
                        candies_to_give[i] = last_amount + 1
                        last_amount += 1
                    else:
                        break

        # Return the total candy given out
        return sum(candies_to_give)
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's two example cases.
- Lots of gas at the last station.
- Single child
- Two children
- All equal children
- An ascending/descending list
- Lowest-rating in middle
- Highest-rating in middle
- Variations of peaks and plateaus
- Variations of 1000-long cases

```text
** Unit Tests **

Unit Tests Ran: 18
Methods Tested: 4
Errors: 0
Skipped: 0
Failures: 0
```

### Code Coverage

We received 100% code coverage of all methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
call_tests.py        13      0   100%
candy.py             59      0   100%
candy_2.py           17      0   100%
candy_3.py           11      0   100%
candy_4.py           24      0   100%
memory_tests.py      51      0   100%
testcases.py         88      0   100%
time_tests.py        53      1    98%   111
unit_tests.py       192      0   100%
-----------------------------------------------
TOTAL               508      1    99%
```

`time_tests.py` coverage can be ignored.

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests**

Case 10: 1000-long. Alternating high and low.
    candy_2(): 12682 blocks
    candy_3(): 25989 blocks
      candy(): 63090 blocks
    candy_4(): 156433 blocks

Case 11: 1000-long. All equal ratings.
    candy_2(): 12682 blocks
      candy(): 18010 blocks
    candy_3(): 18029 blocks
    candy_4(): 79009 blocks

Case 12: 1000-long. Ascending.
    candy_2(): 12682 blocks
    candy_3(): 41789 blocks
      candy(): 41850 blocks
    candy_4(): 94673 blocks

Case 13: Mixed case.
      candy(): 12675 blocks
    candy_2(): 12682 blocks
    candy_3(): 12682 blocks
    candy_4(): 12682 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Case 10: 1000-long. Alternating high and low.
    candy_2() runtime: 3.502 x (10 ^ -1) sec
    candy_3() runtime: 3.941 x (10 ^ -1) sec
    candy_4() runtime: 1.215 x (10 ^ +0) sec
      candy() runtime: 1.633 x (10 ^ +0) sec

Case 11: 1000-long. All equal ratings.
    candy_3() runtime: 1.117 x (10 ^ -1) sec
    candy_2() runtime: 1.413 x (10 ^ -1) sec
      candy() runtime: 4.184 x (10 ^ -1) sec
    candy_4() runtime: 4.279 x (10 ^ -1) sec

Case 12: 1000-long. Ascending.
    candy_2() runtime: 1.525 x (10 ^ -1) sec
    candy_3() runtime: 1.649 x (10 ^ -1) sec
      candy() runtime: 5.327 x (10 ^ -1) sec
    candy_4() runtime: 5.729 x (10 ^ -1) sec

Case 13: Mixed case.
    candy_2() runtime: 4.149 x (10 ^ -3) sec
    candy_3() runtime: 4.376 x (10 ^ -3) sec
    candy_4() runtime: 1.289 x (10 ^ -2) sec
      candy() runtime: 1.569 x (10 ^ -2) sec
```

## Reflections

I spend time on this problem updating the memory tests to be easier to copy-paste between problems.

## Solution Variations

### candy_2.py

```python
class Solution:
    def candy_2(self, ratings: list[int]) -> int:
        length = len(ratings)
        total, up, down, peak = 1, 0, 0, 1
        for idx in range(1, length):
            prev, curr = ratings[idx - 1], ratings[idx]
            if curr > prev:
                up += 1
                total += 1 + up
                peak, down = 1 + up, 0
            elif curr < prev:
                down += 1
                total += down + int(peak <= down)
                up = 0
            else:
                up, down, peak = 0, 0, 1
                total += 1
        return total
```

### candy_3.py

```python
class Solution:
    def candy_3(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
```

### candy_4.py

```python
class Solution:
    def candy_4(self, ratings: list[int]) -> int:
        self.ratings = ratings
        self.candies = {}
        for i in range(len(ratings)):
            self.dfs(i)
        return sum(self.candies.values())
    def dfs(self, ind):
        if ind in self.candies:
            return self.candies[ind]
        val = self.ratings[ind]
        left = self.ratings[ind - 1] if ind - 1 >= 0 else val
        right = self.ratings[ind + 1] if ind + 1 < len(self.ratings) else val
        if val > left and val > right:
            left_candy = self.dfs(ind - 1)
            right_candy = self.dfs(ind + 1)
            candy = max(left_candy, right_candy) + 1
        elif val > left:
            candy = self.dfs(ind - 1) + 1
        elif val > right:
            candy = self.dfs(ind + 1) + 1
        else:
            candy = 1
        self.candies[ind] = candy
        return self.candies[ind]
```
