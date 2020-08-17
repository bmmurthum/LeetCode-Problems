# Word Search

**Description:**

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**
```
board = [['A','B','C'],
         ['D','E','F'],
         ['G','H','I']]
 word = "ABC", returns TRUE.
 word = "EHI", returns TRUE.
 word = "AEI", returns FALSE. No diagonals.
 word = "ABD", returns FALSE. "B" and "D" not connected.
 word = "ABA", returns FALSE. No repeated characters.
```

## Additional Details

The code deliverable for LeetCode was the Solution class included in the source code. The rest of my exercise was an exercise in a variety of things.
- Displaying the tables and data for troubleshooting and aesthetic
- Writing valuable documentation and comments
- Writing code for comparison of runtimes of various cases

There were some particular optimizations that I put particular attention to.
- There was an eye to reduction of memory calls, for the sake of efficiency, particularly within the recursive method.
- With an understanding that the array boards could become very large, causing much effort to be put on the recursive algorithm, I made sure to include a speedy, preliminary test to check for the possibility of finding the word. This reduced runtimes dramatically for these cases of false-returns.

## Further Inquiry

- Have this functionality be able to search boards loaded from a text file
- Have the boards be randomly, or semi-randomly, generated
- Have the boards be generated with guaranteed solutions
- Optimize the efficiency
- Have the boards be output to an HTML page
