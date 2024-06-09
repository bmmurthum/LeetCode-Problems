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
    
    # # Someone else's solution
    # def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
    #     magazine = [letter for letter in magazine]
    #     for letter in ransomNote:
    #         if letter not in magazine:
    #             return False
    #         else:
    #             magazine.remove(letter)
    #     return True
    
    # # Someone else's solution
    # def canConstruct_3(self, ransomNote: str, magazine: str) -> bool:
    #     letter_count_m = dict()
    #     for char in magazine:
    #         if char in letter_count_m.keys():
    #             letter_count_m[char]+=1
    #         else:
    #             letter_count_m[char] = 1
    #     for char in ransomNote:
    #         if char not in letter_count_m:
    #             return False
    #         if letter_count_m[char]<=0:
    #             return False
    #         else:
    #             letter_count_m[char]-=1
    #     return True
    
    # # Someone else's solution
    # def canConstruct_4(self, ransomNote: str, magazine: str) -> bool:
    #     for let in ransomNote:
    #             if let in magazine:
    #                 ind = magazine.find(let)
    #                 magazine = magazine[:ind] + magazine[ind + 1:]
    #             else:
    #                 return False
    #     return True
    
    # # Someone else's solution
    # def canConstruct_5(self, ransomNote: str, magazine: str) -> bool:
    #     for ch in ransomNote:
    #         if ch in magazine:
    #             magazine = magazine.replace(ch,"",1)
    #         else:
    #             return False
    #     return True