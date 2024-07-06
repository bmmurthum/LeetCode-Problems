# H-Index

**Description:**

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `ith` paper, return the researcher's h-index.

According to the definition of [h-index](https://en.wikipedia.org/wiki/H-index) on Wikipedia: The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

**Examples:**

```text
Input: citations = [3,0,6,1,5]
Output: 3

Input: citations = [1,3,1]
Output: 1
```

## Overview

My solution just sorts it largest to smallest and then when iterating through, sees when the index is larger than the value and returns that index. Badaboom.

The ending `return len(citation)` catches any cases where the values are all higher than the length of the list. In this case, the minimum value between (1) the length of the list and (2) the smallest number of citations will be the length of the list, thus the h-index.

**First Solution:**

```python
def h_index(self, citations: list[int]) -> int:
    """
    Return the H-Index value of a group of an author's papers, given each
    item in the list is a paper's number of citations.

    Args:
        `citations`: A list of number of citations that each published
            paper by this author has.
    Returns:
        `h_index`: The value.
    """
    citations.sort(reverse=True)
    for i, val in enumerate(citations):
        if i >= val:
            return i
    return len(citations)
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and general confidence.

We ran this for my solution and another person's solution.

We checked for:

- LeetCode's two example cases
- One item:
  - With value of `1`. One citation on one paper.
  - With value of `0`. Zero citations on one paper.
  - With value of `9`. Larger than length.
- Two items, each with value of `2`.
- Three twos `[2,2,2]`. Each citation number lower than the length.
- Three fours `[4,4,4]`. Total length lower than minimum citations.
- A generated list with 2000 zeroes, then three `3`.

### Code Coverage

We received 100% code coverage on my method and others' from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run -m unittest
> coverage report
Name                  Stmts   Miss  Cover
-----------------------------------------
h_index.py                7      0   100%
other_solution_2.py      10      0   100%
test_unit_tests.py       99      0   100%
testcases.py             47      0   100%
-----------------------------------------
TOTAL                   163      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution `h_index()` against one other person's solution `h_index_2()`.

**Test 10:** A generated list of two thousand `0`, then three `3`.

Memory blocks used:

- `h_index()`: 488 blocks
- `h_index_2()`: 464 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on a test cases.

**Test 10:** A generated list of two thousand `0`, then three `3`.

- `h_index()`: 0.708 x 10^-5 sec
- `h_index_2()`: 5.596 x 10^-5 sec

**Test 7:** A list of 15 scrambled values.

- `h_index()`: 2.965 x 10^-7 sec
- `h_index_2()`: 9.385 x 10^-7 sec

## Reflections

This was simpler than I expected. If there's an algorithm for doing this without a sort that is faster I'd be surprised.

## Solution Variations

### other_solution_2.py

Why's this person complicating it?

```python
class Solution:
    def h_index_2(self, citations: list[int]) -> int:
        count = [0] * (max(citations) + 1)
        for c in citations:
            count[c] += 1
        paper_count = 0
        for number_cited in range(len(count) - 1, -1, -1):
            paper_count += count[number_cited]
            if paper_count >= number_cited:
                return number_cited
```
