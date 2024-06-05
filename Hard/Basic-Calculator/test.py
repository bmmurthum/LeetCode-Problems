import unittest
from basicCalculator import Solution

class testing(unittest.TestCase):

    # Testing simple case.
    def test_1(self):
        sol = Solution()
        s = "1 + 1"
        result = sol.calculate(s)
        correctSolution = 2
        self.assertEqual(result, correctSolution, 'The result is incorrect.')

    # Testing case with spaces
    def test_2(self):
        sol = Solution()
        s = " 2   -1+    2     "
        result = sol.calculate(s)
        correctSolution = 3
        self.assertEqual(result, correctSolution, 'Case with spaces')

    # Testing case with negative values
    def test_3(self):
        sol = Solution()
        s = "-2-1 - 2 "
        result = sol.calculate(s)
        correctSolution = -5
        self.assertEqual(result, correctSolution, 'Case with spaces and negative values.')

    # Testing simple case wrapped in parentheses
    def test_4(self):
        sol = Solution()
        s = "(1+3)"
        result = sol.calculate(s)
        correctSolution = 4
        self.assertEqual(result, correctSolution, 'Simple case wrapped in parentheses.')

    # Testing "-" before an open parenthesis. At beginning.
    def test_5(self):
        sol = Solution()
        s = "-(1+2)+(3+4)"
        result = sol.calculate(s)
        correctSolution = 4
        self.assertEqual(result, correctSolution, 'Testing "-" before an open parenthesis. At beginning.')

    # Testing "-" before an open parenthesis. Testing negative numbers.
    def test_6(self):
        sol = Solution()
        s = "-3 + 23 - (-2 - 1)"
        result = sol.calculate(s)
        correctSolution = 23
        self.assertEqual(result, correctSolution, 'Testing "-" before an open parenthesis. Testing negative numbers.')

    # Testing complicated case
    def test_7(self):
        sol = Solution()
        s = "-(-235 + (-2 - 1 + 3 + 6))"
        result = sol.calculate(s)
        correctSolution = 229
        self.assertEqual(result, correctSolution, 'Testing complicated case.')

    # Testing parentheses after another
    def test_8(self):
        sol = Solution()
        s = "(1+2+3)+(2+5)+(5+6)"
        result = sol.calculate(s)
        correctSolution = 24
        self.assertEqual(result, correctSolution, 'Testing parentheses after another.')

    # Testing nested parentheses
    def test_9(self):
        sol = Solution()
        s = "(1+(2+(3+(4+5)+(6+7))))"
        result = sol.calculate(s)
        correctSolution = 28
        self.assertEqual(result, correctSolution, 'Testing parentheses after another.')
    
    # Testing nested parentheses. Negative numbers.
    def test_10(self):
        sol = Solution()
        s = "-(1-(2-(3-4)))"
        result = sol.calculate(s)
        correctSolution = 2
        self.assertEqual(result, correctSolution, 'Testing parentheses after another.')

    # Testing nested parentheses. Negative numbers.
    def test_11(self):
        sol = Solution()
        s = "- (3 - (- (4 + 5) ) )"
        result = sol.calculate(s)
        correctSolution = -12
        self.assertEqual(result, correctSolution, 'Testing parentheses after another.')

if __name__ == '__main__':
    unittest.main()