import tracemalloc

class Solution:
    def canConstruct_1(self, ransomNote: str, magazine: str) -> bool:
        '''
        Returns `True` if for every letter in `ransomNote` list, there is a letter in `magazine`.
        '''
        uniqueLetters = set(ransomNote)
        for letter in uniqueLetters:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
    
    # Someone else's solution
    def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
        magazine = [letter for letter in magazine]
        for letter in ransomNote:
            if letter not in magazine:
                return False
            else:
                magazine.remove(letter)
        return True
    
    # Someone else's solution
    def canConstruct_3(self, ransomNote: str, magazine: str) -> bool:
        letter_count_m = dict()
        for char in magazine:
            if char in letter_count_m.keys():
                letter_count_m[char]+=1
            else:
                letter_count_m[char] = 1
        for char in ransomNote:
            if char not in letter_count_m:
                return False
            if letter_count_m[char]<=0:
                return False
            else:
                letter_count_m[char]-=1
        return True
    
    # Someone else's solution
    def canConstruct_4(self, ransomNote: str, magazine: str) -> bool:
        for let in ransomNote:
                if let in magazine:
                    ind = magazine.find(let)
                    magazine = magazine[:ind] + magazine[ind + 1:]
                else:
                    return False
        return True
    
    # Someone else's solution
    def canConstruct_5(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch in magazine:
                magazine = magazine.replace(ch,"",1)
            else:
                return False
        return True


# Testing Memory Allocation
# canConstruct_1()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
tracemalloc.start()
s = Solution()
result = s.canConstruct_1(ransomNote,magazine)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("canConstruct_1(): " + tracedMemoryPeak + " blocks")


# Testing Memory Allocation
# canConstruct_2()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
tracemalloc.start()
s = Solution()
result = s.canConstruct_2(ransomNote,magazine)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("canConstruct_2(): " + tracedMemoryPeak + " blocks")


# Testing Memory Allocation
# canConstruct_3()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
tracemalloc.start()
s = Solution()
result = s.canConstruct_3(ransomNote,magazine)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("canConstruct_3(): " + tracedMemoryPeak + " blocks")


# Testing Memory Allocation
# canConstruct_4()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
tracemalloc.start()
s = Solution()
result = s.canConstruct_4(ransomNote,magazine)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("canConstruct_4(): " + tracedMemoryPeak + " blocks")


# Testing Memory Allocation
# canConstruct_5()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
tracemalloc.start()
s = Solution()
result = s.canConstruct_5(ransomNote,magazine)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("canConstruct_5(): " + tracedMemoryPeak + " blocks")