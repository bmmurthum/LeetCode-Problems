# Group Anagrams

**Description:**

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints: 
- `1 <= s.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.


**Example:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
```


## Overview

My solution iterates through the list of words to create a matching-size list of each word's hash value `hashMap`. We remove duplicates from this list and save it as a new list `newHashMap`. This will be a guide for finding appropriate indexes of hashes for our return list. We then walk through the initial word list a second time to add each word to its appropriate list inside the `outputList` as it's hash matches a hash from the `newHashMap`.

We sort the internal lists and the containing list for comparison in testing.

```python3
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Build an associated list of hashes for each word
        hashMap = []
        for word in range(0,len(strs)):
            hashVal = 0
            for letter in strs[word]:
                hashVal += hash(letter)
            hashMap.append(hashVal)
        # Remove duplicates in the hashmap
        newHashMap = list(set(hashMap))
        # Create correct number of internal lists for output list
        outputList = []
        for i in range(len(newHashMap)):
            outputList.append([])
        # Append the current word to the correct list
        for word in range(0,len(strs)):
            currentWordHash = hashMap[word]
            i = newHashMap.index(currentWordHash)
            outputList[i].append(strs[word])
        # Sort for testing comparision
        for i in outputList:
            i.sort()
        outputList = sorted(outputList, key=lambda x: x[0])
        return outputList
```

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/Group-Anagrams/test.py) for this problem with `import unittest`. Tests were made for:
- A simple collection
- An empty collection
- A collection with only a single word
- A larger collection

## Reflections

I had some trouble getting a comparison of correct outputs for the testing suite. Various sort methods would give alternating results. I tried casting the lists as `set` to remove the interest in the order of the internal lists, but this throws an error in that the internal lists are incompatible.

I also tried sorting by internal list length. In that case, multiple lists of same size are indeterminately ordered.

My solution here was sorting the internal lists, then the overall list by the first word of each internal list.