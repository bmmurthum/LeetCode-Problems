import unittest
from removeElement import Solution

class testing(unittest.TestCase):

    # Testing simple case.
    def test_1(self):
        nums = [3,2,2,3]
        val = 3
        correctSolution = 2

        resultList = assertCheck(nums, val, correctSolution)
        correctSolutionList = [correctSolution, False, True, True]
        self.assertEqual(resultList, correctSolutionList, 'The result is incorrect.')

    # Testing simple case.
    def test_2(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        correctSolution = 5

        resultList = assertCheck(nums, val, correctSolution)
        correctSolutionList = [correctSolution, False, True, True]
        self.assertEqual(resultList, correctSolutionList, 'The result is incorrect.')

    # Testing removal at end of list.
    def test_3(self):
        nums = [1,2,3,4,5]
        val = 5
        correctSolution = 4

        resultList = assertCheck(nums, val, correctSolution)
        correctSolutionList = [correctSolution, False, True, True]
        self.assertEqual(resultList, correctSolutionList, 'The result is incorrect.')

    # Testing removal at beginning of list.
    def test_4(self):
        nums = [1,2,3,4,5]
        val = 1
        correctSolution = 4

        resultList = assertCheck(nums, val, correctSolution)
        correctSolutionList = [correctSolution, False, True, True]
        self.assertEqual(resultList, correctSolutionList, 'The result is incorrect.')

    # Testing all removal except last.
    def test_5(self):
        nums = [2,2,2,2,4]
        val = 2
        correctSolution = 1

        resultList = assertCheck(nums, val, correctSolution)
        correctSolutionList = [correctSolution, False, True, True]
        self.assertEqual(resultList, correctSolutionList, 'The result is incorrect.')

    # Testing all removal except first.
    def test_6(self):
        nums = [4,2,2,2,2]
        val = 2
        correctSolution = 1

        resultList = assertCheck(nums, val, correctSolution)
        correctSolutionList = [correctSolution, False, True, True]
        self.assertEqual(resultList, correctSolutionList, 'The result is incorrect.')

    # Testing all removal from list.
    def test_7(self):
        nums = [2,2,2,2,2]
        val = 2
        correctSolution = 0

        resultList = assertCheck(nums, val, correctSolution)
        correctSolutionList = [correctSolution, False, True, True]
        self.assertEqual(resultList, correctSolutionList, 'The result is incorrect.')


'''
For each case, we're checking on:
- The parameter "nums" being changed without removing items
- That the beginning up to the length of considered-removed items
  doesn't contain any values matching our "val" parameter.
- That these beginning items contain the same amount of each unique
  item as the initial "nums" input.
'''
def assertCheck(n: list[int], v: int, c: int):
    sol = Solution()
    nums = n
    val = v
    initialNums = nums.copy()
    result = sol.removeElement(nums,val)

    # Check that beginning list doesn't contain a "val"
    valCount = initialNums.count(val)
    correctNewLength = len(initialNums) - valCount
    anyValInNewLength = False
    if nums[:correctNewLength].count(val) == 0:
        anyValInNewLength = False
    else:
        anyValInNewLength = True

    # Check that list length is same size as before
    inputOutputSameListLength = (len(nums) == len(initialNums))

    # Check that the counts of all other values are the same
    setNums = set(initialNums)
    setNums.remove(val)
    sameCounts = True
    for item in setNums:
        if initialNums.count(item) != nums[:correctNewLength].count(item):
            sameCounts = False
    resultList = [result, anyValInNewLength, inputOutputSameListLength, sameCounts]
    return resultList

if __name__ == '__main__':
    unittest.main()