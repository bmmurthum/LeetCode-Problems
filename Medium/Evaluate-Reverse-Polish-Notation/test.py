import unittest
from evaluateReversePolistNotation import Solution

class testing(unittest.TestCase):

    # Testing simple case.
    def test_1(self):
        s = Solution()
        tokens = ["2","1","+","3","*"]
        result = s.evalRPN(tokens)
        correctSolution = 9
        self.assertEqual(result, correctSolution, 'The result is incorrect.')

    # Testing simple case.
    def test_2(self):
        s = Solution()
        tokens = ["4","13","5","/","+"]
        result = s.evalRPN(tokens)
        correctSolution = 6
        self.assertEqual(result, correctSolution, 'The result is incorrect.')

    # Testing longer case.
    def test_3(self):
        s = Solution()
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        result = s.evalRPN(tokens)
        correctSolution = 22
        self.assertEqual(result, correctSolution, 'The result is incorrect.')

    # Testing simple case.
    def test_4(self):
        s = Solution()
        tokens = ["4","-2","/","2","-3","-","-"]
        result = s.evalRPN(tokens)
        correctSolution = -7
        self.assertEqual(result, correctSolution, 'The result is incorrect.')

if __name__ == '__main__':
    unittest.main()