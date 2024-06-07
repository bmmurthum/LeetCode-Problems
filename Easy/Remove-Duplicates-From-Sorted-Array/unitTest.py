import unittest
from removeDuplicatesFromSortedArray import Solution

class testing(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    # Testing simple case.
    def test_1(self):
        nums = [1,1,2]
        correctNums = [1,2]
        correctSolution = 2

        result = self.sol.removeDuplicates_1(nums)
        matchedFirstValues = matchedValues(nums,correctNums,correctSolution)

        resultList = [result, matchedFirstValues]
        correctList =[correctSolution, True]
        self.assertEqual(resultList, correctList, 'The result is incorrect on simple case.')

    # Testing simple case.
    def test_2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        correctNums = [0,1,2,3,4]
        correctSolution = 5

        result = self.sol.removeDuplicates_1(nums)
        matchedFirstValues = matchedValues(nums,correctNums,correctSolution)
        resultList = [result, matchedFirstValues]
        correctList =[correctSolution, True]
        self.assertEqual(resultList, correctList, 'The result is incorrect on simple case.')

    # Testing case with negatives.
    def test_3(self):
        nums = [-3,-2,-2,-1,0,1,2,3,3]
        correctNums = [-3,-2,-1,0,1,2,3]
        correctSolution = 7

        result = self.sol.removeDuplicates_1(nums)
        matchedFirstValues = matchedValues(nums,correctNums,correctSolution)
        resultList = [result, matchedFirstValues]
        correctList =[correctSolution, True]
        self.assertEqual(resultList, correctList, 'The result is incorrect on simple case.')

    # Testing case with single item.
    def test_4(self):
        nums = [1]
        correctNums = [1]
        correctSolution = 1

        result = self.sol.removeDuplicates_1(nums)
        matchedFirstValues = matchedValues(nums,correctNums,correctSolution)
        resultList = [result, matchedFirstValues]
        correctList =[correctSolution, True]
        self.assertEqual(resultList, correctList, 'The result is incorrect on simple case.')

    # Testing case with longer chain of same values.
    def test_5(self):
        nums = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6,7,8,9,10]
        correctNums = [1,2,3,4,5,6,7,8,9,10]
        correctSolution = 10

        result = self.sol.removeDuplicates_1(nums)
        matchedFirstValues = matchedValues(nums,correctNums,correctSolution)
        resultList = [result, matchedFirstValues]
        correctList =[correctSolution, True]
        self.assertEqual(resultList, correctList, 'The result is incorrect on simple case.')


def matchedValues(nums, correctNums, k):
    """
    Check if the first `k` elements of `nums` match the first `k` elements of `correctNums`.
    Args:
        `nums` (list): A list of integers.
        `correctNums` (list): A list of integers.
        `k` (int): The number of elements to compare.
    Returns:
        bool: True if the first `k` elements of `nums` match the first `k` elements of `correctNums`, False otherwise.
    """
    for i in range(k):
        if nums[i] != correctNums[i]:
            return False
    return True
    

if __name__ == '__main__':
    unittest.main()