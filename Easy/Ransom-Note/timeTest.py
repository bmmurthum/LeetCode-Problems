import timeit
numTests = 100

# My solution
mycode = '''
class Solution:
    def canConstruct_1(self, ransomNote: str, magazine: str) -> bool:
        uniqueLetters = set(ransomNote)
        for letter in uniqueLetters:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
s = Solution()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
result = s.canConstruct_1(ransomNote,magazine)
'''
timePerRun = str(timeit.timeit(stmt=mycode,number=numTests)/numTests)
print("canConstruct_1():" + timePerRun)


# Someone else's solution
mycode = '''
class Solution:
    def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
        magazine = [letter for letter in magazine]
        for letter in ransomNote:
            if letter not in magazine:
                return False
            else:
                magazine.remove(letter)
        return True
s = Solution()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
result = s.canConstruct_2(ransomNote,magazine)
'''
timePerRun = str(timeit.timeit(stmt=mycode,number=numTests)/numTests)
print("canConstruct_2():" + timePerRun)


# Someone else's solution
mycode = '''
class Solution:
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
s = Solution()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
result = s.canConstruct_3(ransomNote,magazine)
'''
timePerRun = str(timeit.timeit(stmt=mycode,number=numTests)/numTests)
print("canConstruct_3():" + timePerRun)


# Someone else's solution
mycode = '''
class Solution:
    def canConstruct_4(self, ransomNote: str, magazine: str) -> bool:
        for let in ransomNote:
                if let in magazine:
                    ind = magazine.find(let)
                    magazine = magazine[:ind] + magazine[ind + 1:]
                else:
                    return False
        return True
s = Solution()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
result = s.canConstruct_4(ransomNote,magazine)
'''
timePerRun = str(timeit.timeit(stmt=mycode,number=numTests)/numTests)
print("canConstruct_4():" + timePerRun)


# Someone else's solution
mycode = '''
class Solution:
    def canConstruct_5(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch in magazine:
                magazine = magazine.replace(ch,"",1)
            else:
                return False
        return True
s = Solution()
ransomNote = "aabcdefghijklmnopqrstuvwxyzzzzzz"
magazine = "aabcdefghijklmnopqrstuvwxyzzzzzz"
result = s.canConstruct_5(ransomNote,magazine)
'''
timePerRun = str(timeit.timeit(stmt=mycode,number=numTests)/numTests)
print("canConstruct_5():" + timePerRun)