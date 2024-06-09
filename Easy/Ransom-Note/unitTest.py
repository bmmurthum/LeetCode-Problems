import unittest
from ransomNote import Solution

class testing(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    # Testing no matches.
    def test_noMatches(self):
        ransomNote = "a"
        magazine = "b"
        correctSolution = False
        result = self.sol.canConstruct_1(ransomNote,magazine)
        self.assertEqual(result, correctSolution, 'The result is incorrect on no-matches case.')

    # Testing single letter.
    def test_singleLetterMatching(self):
        ransomNote = "c"
        magazine = "c"
        correctSolution = True
        result = self.sol.canConstruct_1(ransomNote,magazine)
        self.assertEqual(result, correctSolution, 'The result is incorrect on single letter case.')

    # Testing not enough matches.
    def test_notEnoughMatches(self):
        ransomNote = "aa"
        magazine = "ab"
        correctSolution = False
        result = self.sol.canConstruct_1(ransomNote,magazine)
        self.assertEqual(result, correctSolution, 'The result is incorrect on not enough of our desired letter case.')

    # Testing no magazine letters
    def test_noMagazineItems(self):
        ransomNote = "hello world"
        magazine = ""
        correctSolution = False
        result = self.sol.canConstruct_1(ransomNote,magazine)
        self.assertEqual(result, correctSolution, 'The result is incorrect on empty magazine case.')

    # Testing that it does not handle spaces
    def test_handleSpaces(self):
        ransomNote = "hi mom"
        magazine = "himom"
        correctSolution = True
        result = self.sol.canConstruct_1(ransomNote,magazine)
        self.assertNotEqual(result, correctSolution, 'The result is incorrect on spaces case.')

 
if __name__ == '__main__':
    unittest.main()