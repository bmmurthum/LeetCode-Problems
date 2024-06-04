import unittest
from validAnagram import Solution

class isAnagram(unittest.TestCase):

    # Testing simple case.
    def test_1(self):
        s = "anagram"
        t = "nagaram"
        correctSolution = True
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing simple case.
    def test_2(self):
        s = "rat"
        t = "car"
        correctSolution = False
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing on my algorithm's length and hash.
    def test_3(self):
        s = "bbbbb"
        t = "f"
        correctSolution = False
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
    
    # Testing identical case
    def test_4(self):
        s = "racecar"
        t = "racecar"
        correctSolution = True
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing complete differences case
    def test_5(self):
        s = "a"
        t = "b"
        correctSolution = False
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing empty 't' value. Within scope of given constraints.
    def test_6(self):
        s = "a"
        t = ""
        correctSolution = False
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing 't' value being longer than 's'
    def test_7(self):
        s = "a"
        t = "apple"
        correctSolution = False
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing 's' value being longer than 't'
    def test_8(self):
        s = "banana"
        t = "z"
        correctSolution = False
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing flipped word
    def test_9(self):
        s = "banana"
        t = "ananab"
        correctSolution = True
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing anagram. Correct solution.
    def test_10(self):
        s = "dusty"
        t = "study"
        correctSolution = True
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing anagram. Correct solution.
    def test_11(self):
        s = "players"
        t = "parsley"
        correctSolution = True
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing hash
    def test_12(self):
        s = "ac"
        t = "bb"
        correctSolution = False
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing edge case
    def test_12(self):
        s = "a"
        t = "a"
        correctSolution = False
        testCase = Solution()
        result = testCase.isAnagram(s,t)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')

if __name__ == '__main__':
    unittest.main()