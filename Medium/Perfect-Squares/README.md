# Perfect Squares

**Description:**

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

**Example:**
```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

**To Run:**

To run this program, make sure you have Java. The solution is written in Java 1.0.8. You may have to confirm that Java is included in your `PATH` variables. Navigate to the directory containing the file `perfectSquares.java`.

- Compile the program: `$ javac perfectSquares.java`
- Run the program with Java with: `$ java perfectSquares`

Running this program as given runs the solution-algorithm through 40 given test cases and reports percentage of success.

## Overview

## Reflections

## Further Inquiry

## Test Cases

**Case 1:** A square.
```
Input: 4
Output: 1  
```

**Case 2:** A number non-square.
```
Input: 3
Output: 3
Explanation: 1 + 1 + 1
```

**Case 3:** Zero.
```
Input: 0
Output: 0
```

**Case 4:** Minimum of multiple answers.
```
Input: 12
Output: 3
Explanation: 4 + 4 + 4, not 9 + 1 + 1 + 1
```

**Case 5:** A number non-square.
```
Input: 13
Output: 2
```
