import unittest
from simplifyPath import Solution

class TestSimplifyPath(unittest.TestCase):

    # Testing simple case.
    def test_1(self):
        path = "/home//foo/"
        correctSolution = "/home/foo"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing simple case.
    def test_2(self):
        path = "/home/"
        correctSolution = "/home"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')

    # Testing applying 'move up folder'.
    def test_3(self):
        path = "/home/user/Documents/../Pictures"
        correctSolution = "/home/user/Pictures"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing case of trying to go above root folder.
    def test_4(self):
        path = "/../"
        correctSolution = "/"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing three dots and general application
    def test_5(self):
        path = "/.../a/../b/c/../d/./"
        correctSolution = "/.../b/d"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing three dots
    def test_6(self):
        path = "/home/a/b/.../c/d/"
        correctSolution = "/home/a/b/.../c/d"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing going up multiple directories
    def test_7(self):
        path = "/home/a/b/c/../../../d/"
        correctSolution = "/home/d"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')

    # Testing going up multiple directories
    def test_8(self):
        path = "/a/../../b/../c//.//"
        correctSolution = "/c"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')

    # Testing multiple forward slashes
    def test_9(self):
        path = "/a//b////c/d//././/.."
        correctSolution = "/a/b/c"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing multiple up directories towards root
    def test_10(self):
        path = "/home/../../.."
        correctSolution = "/"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing current-directory at root
    def test_11(self):
        path = "/."
        correctSolution = "/"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing multiple up directories towards root
    def test_12(self):
        path = "/hzx/.././BVHm/../././..//"
        correctSolution = "/"
        testCase = Solution()
        result = testCase.simplifyPath(path)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')

if __name__ == '__main__':
    unittest.main()