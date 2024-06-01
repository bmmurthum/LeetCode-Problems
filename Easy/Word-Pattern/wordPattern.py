class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        matchDict = dict()
        # If the given pattern length doesn't match the word-count of the word 
        # string, return False.
        if len(pattern) != len(words):
            return False
        # Check the letters of the pattern for if has-been-seen, then if the
        # word associated with it matches with current word being looked at.
        for i in range(len(pattern)):
            # New letter
            if pattern[i] not in matchDict:
                # Is this word already seen? Cannot be new letter.
                if words[i] in matchDict.values():
                    return False
                # Assign to letter
                matchDict[str(pattern[i])] = words[i]
            elif matchDict[pattern[i]] != words[i]:
                return False
        return True