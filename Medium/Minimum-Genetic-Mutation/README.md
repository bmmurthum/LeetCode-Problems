# Minimum Genetic Mutation

**Description:**

A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`.

Suppose we need to investigate a mutation from a gene string `startGene` to a gene string `endGene` where one mutation is defined as one single character changed in the gene string.

For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.
There is also a gene bank `bank` that records all the valid gene mutations. A gene must be in `bank` to make it a valid gene string.

Given the two gene strings `startGene` and `endGene` and the gene bank `bank`, return the minimum number of mutations needed to mutate from `startGene` to `endGene`. If there is no such a mutation, return `-1`.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

**Constraints:**

- `0 <= bank.length <= 10`
- `startGene.length == endGene.length == bank[i].length == 8`
- `startGene`, `endGene`, and `bank[i]` consist of only the characters `['A', 'C', 'G', 'T']`.

**Examples:**

```text
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
```

## Overview

My solution is a breadth-first search that looks at the next item that is one character in difference. We use a helping function `is_one_char_diff()` to check if any strings in the `bank` are valid mutations to traverse to next.

```python
from collections import deque
class Solution:
    """Problem given by LeetCode."""

    def min_mutation(self, start_gene: str, end_gene: str, bank: list[str]) -> int:
        """
        Returns the number of mutations needed to change the beginning
        gene-string to the ending gene-string.

        Args:
            `start_gene`: The starting gene-string.
            `end_gene`: The end gene-string that we desire.
            `bank`: A list of valid genes that give options of mutations.
        Returns:
            `mutation_count`: The number of steps to get to final gene-string.
                Returns `-1` if the final gene-string is unable to be reached.
        """
        # Mutations that have been visited
        visited = []
        visited.append(start_gene)

        # Which mutations to look at next
        queue = deque()
        next_queue = deque()
        queue.append(start_gene)

        # Breadth-first search
        mutation_count = 0
        while queue:
            current = queue.popleft()
            # Stop when found goal.
            if current == end_gene:
                return mutation_count
            # Consider which positions to look at next.
            for _, item in enumerate(bank):
                if self.is_one_char_diff(current, item) and item not in visited:
                    next_queue.append(item)
                    visited.append(item)
            # Set up next steps in queue
            if len(queue) == 0:
                queue = next_queue.copy()
                next_queue.clear()
                mutation_count += 1

        # If never bumped into goal, return -1
        return -1

    def is_one_char_diff(self, a: str, b: str) -> bool:
        """
        Checks to see that the two given strings only have one character
        difference. It requires that the two strings are the same length.

        Args:
            `a`: First string.
            `b`: Second string.
        Returns:
            `True/False`: If there is only one character difference.
        """
        count = 0
        for x, y in zip(a, b):
            if x != y:
                count += 1
        if count == 1:
            return True
        else:
            return False
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and general confidence.

We ran this for my solution and two other people's solutions.

We checked for:

- LeetCode's two example cases.
- Never finding the goal case.
- Taking several steps to find goal.
- Taking two steps with a longer false path.

### Code Coverage

We received 100% code coverage on my methods from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run -m unittest
> coverage report
Name                            Stmts   Miss  Cover
---------------------------------------------------
minimum_genetic_mutation.py        30      0   100%
minimum_genetic_mutation_2.py      30      0   100%
minimum_genetic_mutation_3.py      16      0   100%
test_unittests.py                  69      0   100%
testcases.py                       31      0   100%
---------------------------------------------------
TOTAL                             176      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution `min_mutation()` against the other solutions `min_mutation_2()` and `min_mutation_3()`.

**Test 4:** Takes several steps to find goal string.

Memory blocks used:

- `min_mutation()`: 3264 blocks
- `min_mutation_2()`: 3848 blocks
- `min_mutation_3()`: 2424 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on a test cases.

**Test 4:** Takes several steps to find goal string.

- `min_mutation()`: 3.894 x 10^-5 sec
- `min_mutation_2()`: 4.125 x 10^-5 sec
- `min_mutation_3()`: 5.328 x 10^-5 sec

## Reflections

This is a [edit distance](https://en.wikipedia.org/wiki/Levenshtein_distance) problem at heart. If I wanted to find more optimizations, I'd study the solutions for this sort of problem. In the short term, I could likely optimize my function `is_one_char_diff()` to not be required to iterate through the length of the gene-string. I decided against this in seeing the constraints describing a limited 8 char length.
