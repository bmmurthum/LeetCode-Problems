# Roman to Integer

**Description:**

Seven different symbols represent Roman numerals with the following values:

```text
I -> 1
V -> 5
X -> 10
L -> 50
C -> 100
D -> 500
M -> 1000
```

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
- Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

**Constraints:**

- `1 <= num <= 3999`

**Examples:**

```text
Input: num = 3749
Output: "MMMDCCXLIX"

Input: num = 58
Output: "LVIII"

Input: num = 1994
Output: "MCMXCIV"
```

## Overview

My solution looks at each digit of our given number `num` starting on the right to build a string `output` as we iterate through the digits. For each digit, we can check against a known set `quick_vals` or otherwise follow a pattern to build that digit's substring `temp_output` to then add to the full string.

```python
class Solution:
    """Problem by LeetCode.com"""

    def int_to_roman(self, num: int) -> str:
        """
        Converts a digit [1,3999] to roman numerals.

        Args:
            `num`: The integer format input.
        Returns:
            `output`: The string roman numeral version.
        """

        quick_vals = {
            1: "I",
            4: "IV",
            9: "IX",
            10: "X",
            40: "XL",
            90: "XC",
            100: "C",
            400: "CD",
            900: "CM",
            1000: "M",
            5: "V",
            50: "L",
            500: "D",
        }

        # Handle string building digit by digit.
        num_as_string = str(num)
        decimal = 1
        output = ""
        for i in range(len(num_as_string) - 1, -1, -1):
            value = int(num_as_string[i]) * decimal
            # Handle quick-knowns
            if value in quick_vals:
                output = quick_vals[value] + output
                decimal = decimal * 10
                continue
            # Handle additives
            temp_output = ""
            while value > 0:
                if value >= 1000:
                    temp_output += "M"
                    value -= 1000
                    continue
                elif value >= 500:
                    temp_output += "D"
                    value -= 500
                    continue
                elif value >= 100:
                    temp_output += "C"
                    value -= 100
                    continue
                elif value >= 50:
                    temp_output += "L"
                    value -= 50
                    continue
                elif value >= 10:
                    temp_output += "X"
                    value -= 10
                    continue
                elif value >= 5:
                    temp_output += "V"
                    value -= 5
                    continue
                elif value >= 1:
                    temp_output += "I"
                    value -= 1
                    continue
            output = temp_output + output
            decimal = decimal * 10
        return output
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, covering constraint cases, and general confidence.

We checked for:

- LeetCode's three example cases.
- Bottom of range. 1 -> 10.
- Top of range. 3998 and 3999.

```text
** Unit Tests **

Unit Tests Ran: 18
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
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
call_tests.py              13      0   100%
integer_to_roman.py        45      0   100%
integer_to_roman_2.py       9      0   100%
integer_to_roman_3.py      33      1    97%   29
memory_tests.py            84      0   100%
testcases.py               73      0   100%
time_tests.py              75      0   100%
unit_tests.py             188      0   100%
-----------------------------------------------------
TOTAL                     520      1    99%
```

On the missing `line 29` in `integer_to_roman_3.py`, I don't care to read through their code to find a good unit test to cover that.

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution against the others' solutions.

```text
** Memory Tests **

Testcase 1: LeetCode Example "3749".
    int_to_roman_2(): 683 blocks
    int_to_roman_3(): 873 blocks
      int_to_roman(): 1356 blocks

Testcase 3: LeetCode Example "1994".
    int_to_roman_2(): 664 blocks
    int_to_roman_3(): 865 blocks
      int_to_roman(): 1300 blocks
```

### Process Time Testing

I used `timeit` to isolate the individual functions on a couple test cases. The recorded time represents an average time to find the result once.

```text
** Time Tests **

Testcase 1: LeetCode Example "3749".
    int_to_roman_3() runtime: 5.548 x (10 ^ -4) sec
    int_to_roman_2() runtime: 7.458 x (10 ^ -4) sec
      int_to_roman() runtime: 9.154 x (10 ^ -4) sec

Testcase 3: LeetCode Example "1994".
    int_to_roman_3() runtime: 4.987 x (10 ^ -4) sec
    int_to_roman_2() runtime: 5.763 x (10 ^ -4) sec
      int_to_roman() runtime: 6.944 x (10 ^ -4) sec
```

## Reflections

## Solution Variations

### integer_to_roman_2.py

```python
class Solution:
    def int_to_roman_2(self, num: int) -> str:
        roman_values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        formatted = []
        for v, sym in roman_values:
            while num >= v:
                formatted.append(sym)
                num -= v
        return "".join(formatted)
```

### integer_to_roman_3.py

```python
class Solution:
    def int_to_roman_3(self, num: int) -> str:
        s = [int(c) for c in str(num)]
        n = len(s)

        if s[-1] <= 3:
            rom = "I" * s[-1]
        elif s[-1] == 4:
            rom = "IV"
        elif s[-1] < 9:
            rom = "V" + (s[-1] - 5) * "I"
        elif s[-1] == 9:
            rom = "IX"

        if len(s) > 1:
            if s[-2] <= 3:
                rom = "X" * s[-2] + rom
            elif s[-2] == 4:
                rom = "XL" + rom
            elif s[-2] < 9:
                rom = "L" + (s[-2] - 5) * "X" + rom
            elif s[-2] == 9:
                rom = "XC" + rom

        if len(s) > 2:
            if s[-3] <= 3:
                rom = "C" * s[-3] + rom
            elif s[-3] == 4:
                rom = "CD" + rom
            elif s[-3] < 9:
                rom = "D" + (s[-3] - 5) * "C" + rom
            elif s[-3] == 9:
                rom = "CM" + rom
        if len(s) > 3:
            rom = s[0] * "M" + rom
        return rom
```
