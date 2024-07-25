# Happy Number

**Description:**

Write an algorithm to determine if a number `n` is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` if not.

**Constraints:**

- `1 <= n <= 231 - 1`

**Examples:**

```text
Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

Input: n = 2
Output: false
```

## Overview

My solution looks at the given number `n` and adds it to the set of seen numbers `past_numbers`. If a number from that set is seen again as we process our given number to different numbers in search of `1`, we return `False`. If we reach `1`, we return `True`.

On top of that, we found a selection of numbers `known_false_set` that if stepped into are known to make us return `False` after some amount of iterations. We can be sure to stop a search if we see one of these integers, saving calls on `past_numbers`. So long as the memory cost justifies the performance increase, this is a good deal. This list could be increased to some level to optimize speed further.

```python
class Solution:
    """Problem given by LeetCode."""

    known_false_set = {
        2,3,4,5,6,8,9,11,12,14,15,16,17,18,20,25,26,
        27,29,34,36,37,40,41,42,46,50,52,53,54,58,61,
        64,65,81,85,89,113,145,
    }

    def is_happy_b(self, n: int) -> bool:
        """
        Tells us if an integer is a "happy number."

        Args:
            `n`: Number to look at
        Returns:
            `True/False`: If number is happy.
        """

        past_numbers = set()
        while True:
            if n == 1:
                return True
            elif n in past_numbers or n in self.known_false_set:
                return False
            else:
                past_numbers.add(n)
                temp = str(n)
                total = 0
                for digit in temp:
                    total += (int(digit)) ** 2
                n = total
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and general confidence.

We ran this for my solutions `is_happy()` and `is_happy_b()` and three other people's solutions.

We checked for:

- LeetCode's three example cases.
- All integers between 1 and 20. Hand-checked.
- Three random integers between 1,000 and 10,000. Hand-checked.
- Three random integers between 100,000 and 1,000,000. Hand-checked.

### Code Coverage

We received 100% code coverage on the methods with each test suite using the `coverage.py` tool.

```PowerShell
> coverage run call_tests.py
> coverage report
Name                Stmts   Miss  Cover
---------------------------------------
call_tests.py          13      0   100%
happy_number.py        28      0   100%
happy_number_2.py      12      0   100%
happy_number_3.py       9      0   100%
happy_number_4.py      14      0   100%
memory_tests.py       117      0   100%
testcases.py          105      0   100%
time_tests.py         183      0   100%
unit_tests.py         218      0   100%
---------------------------------------
TOTAL                 699      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solutions against the others' solutions.

**Test 9:** Starting with 8.

- `is_happy()`: 912 blocks
- `is_happy_b()`: 280 blocks
- `is_happy_2()`: 912 blocks
- `is_happy_3()`: 984 blocks
- `is_happy_4()`: 64 blocks

**Test 24:** Starting with 934063.

- `is_happy()`: 912 blocks
- `is_happy_b()`: 403 blocks
- `is_happy_2()`: 912 blocks
- `is_happy_3()`: 984 blocks
- `is_happy_4()`: 128 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on a test case. The recorded time represents an average time to find the result once.

To test a randomly generated group of numbers, I used Python's `time` module to record before and after each process.

The difference in general times between test-24 and test-X seems to be due to the difference in process of finding the result numbers. I have confidence that the numbers within each test group are accurate to what they measure.

**Test 9:** Starting with 8.

- `is_happy()`: 3.4428 x 10^-3 sec
- `is_happy_b()`: 0.1269 x 10^-3 sec
- `is_happy_2()`: 3.5002 x 10^-3 sec
- `is_happy_3()`: 5.5541 x 10^-3 sec
- `is_happy_4()`: 2.5773 x 10^-3 sec

**Test 24:** Starting with 934063.

- `is_happy()`: 5.7992 x 10^-3 sec
- `is_happy_b()`: 1.1242 x 10^-3 sec
- `is_happy_2()`: 4.5403 x 10^-3 sec
- `is_happy_3()`: 5.7238 x 10^-3 sec
- `is_happy_4()`: 5.7150 x 10^-3 sec

**Test X:** Solve many random cases.

- `is_happy()`: 4.1038 x 10^-6 sec
- `is_happy_b()`: 1.9012 x 10^-6 sec
- `is_happy_2()`: 4.2024 x 10^-6 sec
- `is_happy_3()`: 5.4325 x 10^-6 sec
- `is_happy_4()`: 3.8067 x 10^-6 sec

## Reflections

I'm happy to see the battery of known false numbers helped in speed with little memory cost.

During this problem I spent time building an understanding of the `unittest` module, as well as refactoring how I handle my tests. I now have it written such that I can call `coverage` on all the tests simultaneously.

## Solution Variations

### happy_number_2.py

- Had a loose `print()` I had to clean up.
- `sqursum` > `square_sum`
- This is just about identical to mine.

```python
class Solution:
    def is_happy_2(self, n: int) -> bool:
        g = set()
        while n != 1:
            sqarsum = 0
            for i in str(n):
                sqarsum += int(i) ** 2
            n = sqarsum
            if n in g:
                return False
            else:
                g.add(n)
        return True
```

### happy_number_3.py

This person could use a set instead of a dictionary. They almost use `m[n] = 1` to mark a visited integer `n` as visited, but then they use `if n in m`.

I like their `sum([int(x) ** 2 for x in str(n)])`.

```python
class Solution:
    def is_happy_3(self, n: int) -> bool:
        m = dict()
        while n != 1:
            if n in m:
                return False
            m[n] = 1
            n = sum([int(x) ** 2 for x in str(n)])
        return True
```

### happy_number_4.py

What is going on here?!

- `sumSquareDigits()` using `mod` to manipulate individual digits instead of casting. Ok. Is it faster? It's mid-range in performance. The memory is significantly lower with this process.
- They have two separate counts moving through process. One will reach the end and keep staying at `1` if possible. The other catches up, half as fast. In the case of a loop, the fast one will soon be on the same value, causing a break in the loop.

It stands out in doing no casting and its not using of a list of any sort.

```python
class Solution:
    def is_happy_4(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)
        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)
        return True if fast == 1 else False
    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
```
