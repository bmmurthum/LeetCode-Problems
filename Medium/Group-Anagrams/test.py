import unittest
from groupAnagrams import Solution

class groupAnagrams(unittest.TestCase):

    # Testing simple case.
    def test_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        correctSolution = [["bat"],["nat","tan"],["ate","eat","tea"]]
        for i in correctSolution:
            i.sort()
        correctSolution = sorted(correctSolution, key=lambda x: x[0])
        testCase = Solution()
        result = testCase.groupAnagrams(strs)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing simple case.
    def test_2(self):
        strs = [""]
        correctSolution = [[""]]
        testCase = Solution()
        result = testCase.groupAnagrams(strs)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing simple case.
    def test_3(self):
        strs = ["a"]
        correctSolution = [["a"]]
        testCase = Solution()
        result = testCase.groupAnagrams(strs)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')
        
    # Testing simple case.
    def test_4(self):
        strs = ["parsely","inch","chin","players","nchi","bat","tab","abc"]
        correctSolution = [['bat', 'tab'], ['parsely', 'players'], ['abc'], ['inch', 'chin', 'nchi']]
        for i in correctSolution:
            i.sort()
        correctSolution = sorted(correctSolution, key=lambda x: x[0])
        testCase = Solution()
        result = testCase.groupAnagrams(strs)
        self.assertEqual(result, correctSolution, 'The result is incorrect on \
                         simple case.')

if __name__ == '__main__':
    unittest.main()