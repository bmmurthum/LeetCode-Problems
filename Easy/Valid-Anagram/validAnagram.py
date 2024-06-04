class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = 0
        tHash = 0
        for I in range(0,len(s)):
            sHash = sHash + hash(s[I])
        for J in range(0,len(t)):
            tHash = tHash + hash(t[J])
        if len(s) == len(t) and sHash == tHash:
            return True
        else:
            return False