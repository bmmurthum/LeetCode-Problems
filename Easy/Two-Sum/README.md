# Two-Sum

**Description:**

Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:** 
```
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Additional Details

- Returns a vector "[-1,-1]" in the case of failure to find a solution in the list of values.
- Speeds up the search by limiting a potentially long list of integers to the numbers below the target value.
- Speeds up by loop-unrolling with `k=k+4` loop iteration (though very minimal for small lists) in the first loop. Parallel processing could be used effectively on this loop as well.

## Sample Inputs

**Case 1:** Target within list range.
```
nums = [2, 3, 5, 7, 11, 13, 17, 23]
target = 12;
```
**Case 2:** Target above the list.
```
nums = [11, 3, 13, 5, 7, 17, 23]
target = 24;
```
**Case 3:** Target below the list.
```
nums = [5, 7, 11, 13, 17, 23]
target = 4;
```
**Case 4:** Negative number. Unsorted.
```
nums = [-3,4,3,90];
target = 0;
```
**Case 5:** All negative numbers.
```
nums = [-3,-4,-10,-11];
target = -7;
```

## Larger Sets and Data

**UPDATE ME** - This section will show a data set of comparing this solution against others on LeetCode, as well as against the intuitive brute force solution. Add timer to code for performance check. Update code to run independently. 
