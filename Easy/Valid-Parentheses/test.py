import unittest
from validParentheses import Solution

class TestValidParentheses(unittest.TestCase):

    # Testing simple case.
    def test_1(self):
        s = "()"
        correctSolution = True
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')

    # Testing simple case.
    def test_2(self):
        s = "()[]{}"
        correctSolution = True
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')

    # Testing simple incorrect case.
    def test_3(self):
        s = "(]"
        correctSolution = False
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple false case.')

    # Testing incorrect case. Mismatch number of open-close brackets.
    def test_4(self):
        s = "(()"
        correctSolution = False
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         false case. Mismatch number of open-close brackets.')

    # Testing correct case. Brackets within brackets.
    def test_5(self):
        s = "(({[][]}[]))"
        correctSolution = True
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         true case. Brackets within brackets.')

    # Testing incorrect case. Brackets within brackets. Mismatch open-close.
    def test_6(self):
        s = "({[][]}[]))"
        correctSolution = False
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         false case. Mismatch open-close. Brackets within \
                         brackets.')

    # Testing incorrect case. Brackets within brackets. Mismatch open-close.
    def test_7(self):
        s = "["
        correctSolution = False
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         false case. Single bracket.')

    # Testing incorrect case. All left-brackets.
    def test_8(self):
        s = "[[[[[["
        correctSolution = False
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         false case. All left-brackets.')

    # Testing incorrect case. Mismatch open-close. Odd-number string-length.
    def test_9(self):
        s = "((((())))"
        correctSolution = False
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         false case. Odd-number brackets.')
        
    # Testing incorrect case. All right-brackets.
    def test_10(self):
        s = "}}}}}}}"
        correctSolution = False
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         false case. All right-brackets.')
        
    # Testing incorrect case.
    def test_11(self):
        s = "(){}}{"
        correctSolution = False
        testCase = Solution()
        result = testCase.isValid(s)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         false case.')
        

if __name__ == '__main__':
    unittest.main()