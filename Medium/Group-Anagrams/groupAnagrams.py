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