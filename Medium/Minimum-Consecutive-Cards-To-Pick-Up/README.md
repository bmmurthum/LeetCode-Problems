# Minimum Consecutive Cards To Pick Up

**Description:**

You are given an integer array cards where `cards[i]` represents the value of the `ith` card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

Constraints: The length of the list of cards is between 1 and 100,000 inclusive. The values of the cards are between 0 and 1,000,000 inclusive.

**Example:**
```
Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
```

## Overview

My solution notes which "cards" have been seen by adding them to a dictionary as they are seen when iterating through the list. This keeps track of the most recent index that that card has been seen. If that card is seen again, this is a possible solution. We calculate the distance between this index and when it was last seen. If less than a stored minimum, we make this the new minimum.

As we're looking for the minimum of cards possibly picked up to have a match, the logic of the question means that if two are picked up in a row, this is the absolute minimum. My solution stops searching if we find this case. In any other case, we're forced to look at each value in the given list at least once.

## Reflections

To minimize logic, we set the default "minimum" variance of distance between two identical cards to an integer just above the given constraints. If this value is the same by the end of iteration, we know that there is no solution. This could've been done with a `hasFoundSolution` boolean for readability.

The conversion of the integers to strings feels like it may be adding unnecessary burden on memory and computation, but allows us to use a dictionary. Searching a dictionary seems like a good choice on its requiring unique keys. I imagine Python's dictionary has some optimization that I'm cashing in on, as opposed to a simple list.

## Test Cases

**Case 1:** No solution.
```
Input: [1,0,5,3]
Output: -1
```

**Case 2:** Larger solution with smaller solution inside.
```
Input: [3,4,2,4,3,7]
Output: 3
```

**Case 3:** Too little cards given to have a solution. Within given constraints.
```
Input: [1]
Output: -1
```

**Case 4:** Immediate solution, minimal given.
```
Input: [1,1]
Output: 2
```

**Case 5:** Solution within larger list. Can immediately stop iterations.
```
Input: [1,2,3,4,5,6,7,7,8,9,10,1]
Output: 2
```