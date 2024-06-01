import unittest
from wordPattern import Solution

class TestWordPattern(unittest.TestCase):

    # Testing general case.
    def test_1(self):
        pattern = "abba"
        s = "dog cat cat dog"
        correctSolution = True
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on simple case.')

    # Testing an incorrect case.
    def test_2(self):
        pattern = "abba"
        s = "dog cat cat fish"
        correctSolution = False
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on false case.')

    # Testing an incorrect case. No pattern in pattern.
    def test_3(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        correctSolution = False
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on false case.')

    # Testing an correct case. All individual letters and words.
    def test_4(self):
        pattern = "abcd"
        s = "apple banana cat dog"
        correctSolution = True
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on individual words case.')

    # Testing an correct case.
    def test_5(self):
        pattern = "aabbaa"
        s = "dog dog cat cat dog dog"
        correctSolution = True
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on mirror case.')

    # Testing an correct case.
    def test_6(self):
        pattern = "amjxww"
        s = "dog banana tommy john google google"
        correctSolution = True
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on simple case.')

    # Testing an correct case. All the same.
    def test_7(self):
        pattern = "bbbb"
        s = "dog dog dog dog"
        correctSolution = True
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on all-same case.')

    # Testing an incorrent case. Word count doesn't match letter count.
    def test_8(self):
        pattern = "vvv"
        s = "apple apple"
        correctSolution = False
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on mismatch word-letter count case.')

    # Testing an incorrent case. Word count doesn't match letter count.
    def test_9(self):
        pattern = "vvv"
        s = "cat cat cat cat"
        correctSolution = False
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on mismatch word-letter count case.')

    # Testing an incorrect case.
    def test_10(self):
        pattern = "abba"
        s = "dog dog dog dog"
        correctSolution = False
        testCase = Solution()
        result = testCase.wordPattern(pattern, s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on false case.')


if __name__ == '__main__':
    unittest.main()