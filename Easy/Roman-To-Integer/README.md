# Roman to Integer

**Description:**

[Roman numerals](https://en.wikipedia.org/wiki/Roman_numerals) are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol        Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

**Example:**
```
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**To Run:**

To run this program, make sure you have Python 3. The solution is written in Python 3.8.5. Navigate to the file `RomanToInt.py` and run with Python. Running the program as it is provided [here](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Easy/Roman-To-Integer/RomanToInt.py) runs the solution algorithm through 65 test cases. You're welcome to add your own test cases to the initial list. Failed tests output a failure message.

```$ python RomanToInt.py```

## Overview

This problem, focused on processing a string, doesn't call for eyes to parallel-processing, reducing memory usage, or reducing process time. Those would be worthy efforts, but not my desire here. I aimed for a goal of ease in readability and a large set of test-cases, with a partnered testing function to iterate through all the test-cases.

My solution **(1)** translates the string of given characters to their respective numbers, putting them into a list. This allows for a readable and bug-viewable version of code that made for a smooth process of writing the logic. Then, **(2)**, the list is iterated through while looking to both the current value and the next value. This allowed the handling of special cases such as **IX** giving  **9** and **CD** giving **400**. In iteration, if a special case is found, we add that special value to the total, then iterate forward two spaces. If a special case is not found, we simply add the current letter-value to the total and iterate forward. **(3)** Once the iteration is at the last value, or beyond it, the loop exits and the program ends.

## Code Sample

```Python
def romanToInt(s: str) -> int:

  # A list of the initial letters as their represented numbers.
  numberList = []

  # Convert the letters in the string to a list of numbers.
  # For ease of working with logic.
  for letter in s:
      letter = letter.upper()
      if letter == "I":
          numberList.append(1)
      elif letter == "V":
          numberList.append(5)
      elif letter == "X":
          numberList.append(10)
      elif letter == "L":
          numberList.append(50)
      elif letter == "C":
          numberList.append(100)
      elif letter == "D":
          numberList.append(500)
      elif letter == "M":
          numberList.append(1000)

  sum = 0
  currentIndex = 0
  length = len(numberList)
  while True:
      # If done iterating, exit.
      if currentIndex >= length:
          break

      # If at last value in the list.
      if currentIndex == length - 1:
          sum += numberList[currentIndex]
          break

      # Set iterating values.
      currentValue = numberList[currentIndex]
      nextValue = numberList[currentIndex + 1]

      # Unique cases of substraction.
      if currentValue == 1 and nextValue == 5:
          sum += 4
          currentIndex += 2
      elif currentValue == 1 and nextValue == 10:
          sum += 9
          currentIndex += 2
      elif currentValue == 10 and nextValue == 50:
          sum += 40
          currentIndex += 2
      elif currentValue == 10 and nextValue == 100:
          sum += 90
          currentIndex += 2
      elif currentValue == 100 and nextValue == 500:
          sum += 400
          currentIndex += 2
      elif currentValue == 100 and nextValue == 1000:
          sum += 900
          currentIndex += 2
      # All other cases are simple addition to the total.
      else:
          sum += currentValue
          currentIndex += 1

  # Return the total.
  return sum
```

## Reflections

For this program I wanted to first have a grasp on the system of roman numerals to see if I could see any patterns that may be good for the logic of the algorithms. I used [Math Is Fun](https://www.mathsisfun.com/roman-numerals.html) to explore logic and generate test cases. Ultimately, I looked to [LeetCode's](https://leetcode.com/problems/roman-to-integer/) description as if it were the final given code requirements to satisfy. The scope of testing was to directly answer LeetCode's given scope.

## Further Inquiry

1. I'm curious if there's an acceptance of badly written Roman numerals. **IIX** being 8 would be a bad case. I would be interested in writing a validity checker, then writing code that would solve it anyway. It could be that there is multiple solutions to a string.
2. Another further exploration would be seeing how it is used in the current and old world. Is it entirely uncommon to find larger strings? Is it used in math? Should I write curious math algorithms?
3. Certainly, going further in the range of numbers allowed would be another step.
4. Putting some effort toward less memory-usage, or faster process-time would be an exercise.

## Test Cases

**Case 1:** Handles one-character strings.
```
Input: "X"
Output: 10
```

**Case 2:** Accepts lower-case letters.
```
Input: "iii"
Output: 3
```

**Case 3:** A LeetCode example test-case.
```
Input: "MCMXCIV"
Output: 1994
```

**Case 4:** All addition.
```
Input: "CLXVIII"
Output: 168
```

**Case 5:** Two cases of subtraction.
```
Input: "CCCXCIX"
Output: 399
```

**Case 6:** A near-edge case. 11-character string.
```
Input: "MMMCMXCVIII"
Output: 3998
```

**Case 6:** An edge of scope test case.
```
Input: "MMMCMXCIX"
Output: 3999
```
