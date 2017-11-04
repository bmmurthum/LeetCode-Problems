/*

Problem from LeetCode - https://leetcode.com/problems/two-sum/
Author - Brendon Murthum

Given an array of integers, return indices of the two numbers such that they
add up to a specific target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.

- This solution means to speed up the search by limiting a potentially long list
  of integers to the numbers below the target value.
- Speed-up also comes with the loop-unrolling (though very minimal for small
  lists) used in the first loop. Parallel processing could be used effectively
  on the first loop.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Case 1: Target within list range.
nums = [2, 3, 5, 7, 11, 13, 17, 23]
target = 12;

Case 2: Target above the list.
nums = [2, 3, 5, 7, 11, 13, 17, 23]
target = 24;

Case 3: Target below the list.
nums = [5, 7, 11, 13, 17, 23]
target = 4;

Case 4: Negative number. Unsorted.
nums = [-3,4,3,90];
target = 0;

*/

#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /* The given vector-size */
        int size = nums.size();
        /* The vector-size beneath the target value */
        int newSize;
        /* This boolean is used to confirm success */
        bool isFound = false;
        /* This vector stores the two indices of the correct integers */
        vector<int> newVector(2);

        /* Make a copy, that we will sort, then search. */
        vector<int> vectorCopy( nums.size() );
        vectorCopy = nums;

        /* Sort the initial vector */
        std::sort (vectorCopy.begin(), vectorCopy.end());

        /* No need to search for solutations higher than topLimitValue */
        int topLimitValue;
        if (target > 0 && vectorCopy[0] > 0 && target > vectorCopy[0]) {
            topLimitValue = target - vectorCopy[0];
        } else if (target > 0 && vectorCopy[0] < 0 ) {
            topLimitValue = target;
        } else if (target < 0 && vectorCopy[0] < 0) {
            /* Doesn't take advantage of topLimitValue for negative values */
            topLimitValue = vectorCopy[size-1];
        }

        /*
         * This for() to see how many elements are beneath the target value.
         * This may greatly lessen the burden of the following nested loop.
         *
         * The "k=k+4" increment is in favor of loop-unrolling for pipelining.
         * This leads to 4x less jumps/pipeline-pauses, thus speed increase.
         * It also allows for future multiple-simultaneous core use.
        */
        for (int k = 0; k < size; k = k + 4) {
            /* If bumps into value larger than target, stop there */
            if (k == size) {
              newSize = size;
              break;
            }
            if (k < size && vectorCopy[k] > topLimitValue) {
              newSize = k;
              break;
            }
            if (k + 1 == size) {
              newSize = size;
              break;
            }
            if (k + 1 < size && vectorCopy[k+1] > topLimitValue) {
              newSize = k+1;
              break;
            }
            if (k + 2 == size) {
              newSize = size;
              break;
            }
            if(k + 2 < size && vectorCopy[k+2] > topLimitValue) {
              newSize = k+2;
              break;
            }
            if (k + 3 == size) {
              newSize = size;
              break;
            }
            if(k + 3 < size && vectorCopy[k+3] > topLimitValue) {
              newSize = k+3;
              break;
            }
        }

        /* The following displays are for debugging */

        /* Print the original */
        std::cout << "Original Vector: \n";
        std::cout << "[";
        for (int a = 0; a < size - 1; a++) {
            std::cout << nums[a] << ",";
        }
        std::cout << nums[size - 1] << "]\n";

        /* Print the sortedCopy */
        std::cout << "Sorted Vector: \n";
        std::cout << "[";
        for (int a = 0; a < size - 1; a++) {
            std::cout << vectorCopy[a] << ",";
        }
        std::cout << vectorCopy[size - 1] << "]\n";

        /* Print the sizedCopy */
        std::cout << "Sized Vector: \n";
        std::cout << "[";
        for (int a = 0; a < newSize - 1; a++) {
            std::cout << nums[a] << ",";
        }
        std::cout << nums[newSize - 1] << "]\n";


        /* Look for solutions */
        int sortedX, sortedY;
        for (int i = 0; i <= newSize; i++) {
            for (int j = i + 1; j <= newSize; j++) {
                /* If it finds the target, it escapes */
                if (vectorCopy[i] + vectorCopy[j] == target) {
                    isFound = true;
                    sortedX = i;
                    sortedY = j;
                    std::cout << "\nSorted[" << sortedX << "]: " << vectorCopy[i];
                    std::cout << "\nSorted[" << sortedY << "]: " << vectorCopy[j];
                    break;
                }
            }
            if (isFound)
                break;
        }

        /* If found, find original position of numbers */
        bool foundX = false;
        if (isFound) {
            for (int m = 0; m < size; m++) {
                if ((nums[m] == vectorCopy[sortedX] ||
                          nums[m] == vectorCopy[sortedY]) && foundX == false) {
                    newVector[0] = m;
                    foundX = true;
                } else if ((nums[m] == vectorCopy[sortedX] ||
                           nums[m] == vectorCopy[sortedY]) && foundX == true) {
                    newVector[1] = m;
                    break;
                }
            }
        }

        /* Negative result could be handled outside this method */
        if (isFound == false) {
            newVector[0] = -1;
            newVector[1] = -1;
        }

        /* Return the resulting vector */
        return newVector;
    }

};
