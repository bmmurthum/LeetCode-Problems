import unittest
from rotateArray import Solution

class testing(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    # Testing no-rotation case.
    def test_noRotation(self):
        nums = [1,2,3]
        k = 0
        correctSolution = [1,2,3]
        self.sol.rotate_1(nums,k)
        self.assertEqual(nums, correctSolution, 'The result is incorrect on no-rotation case.')

    # Testing single item case.
    def test_singleItem(self):
        nums = [2]
        k = 3
        correctSolution = [2]
        self.sol.rotate_1(nums,k)
        self.assertEqual(nums, correctSolution, 'The result is incorrect on simple case.')

    # Testing rotation matches length case.
    def test_lengthMatchesRotation(self):
        nums = [1,2,3,5]
        k = 4
        correctSolution = [1,2,3,5]
        self.sol.rotate_1(nums,k)
        self.assertEqual(nums, correctSolution, 'The result is incorrect on simple case.')

    # Testing every way of six-item
    def test_sixItems1(self):
        nums = [1,2,3,4,5,6]
        k = 2
        correctSolution = [5,6,1,2,3,4]
        self.sol.rotate_1(nums,k)
        self.assertEqual(nums, correctSolution, 'The result is incorrect on simple case.')

    # Testing every way of six-item
    def test_sixItems2(self):
        nums = [1,2,3,4,5,6]
        k = 3
        correctSolution = [4,5,6,1,2,3]
        self.sol.rotate_1(nums,k)
        self.assertEqual(nums, correctSolution, 'The result is incorrect on simple case.')

    # Testing every way of six-item
    def test_sixItems3(self):
        nums = [1,2,3,4,5,6]
        k = 4
        correctSolution = [3,4,5,6,1,2]
        self.sol.rotate_1(nums,k)
        self.assertEqual(nums, correctSolution, 'The result is incorrect on simple case.')

    # Testing every way of six-item
    def test_sixItems4(self):
        nums = [1,2,3,4,5,6]
        k = 5
        correctSolution = [2,3,4,5,6,1]
        self.sol.rotate_1(nums,k)
        self.assertEqual(nums, correctSolution, 'The result is incorrect on simple case.')

    # Testing prime value length list
    def test_primeLengthList1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        correctSolution = [5,6,7,1,2,3,4]
        self.sol.rotate_1(nums,k)
        self.assertEqual(nums, correctSolution, 'The result is incorrect on simple case.')

    # Testing prime value length list
    def test_primeLengthList2(self):
        nums = [1,2,3,4,5,6,7]
        k = 4
        correctSolution = [4,5,6,7,1,2,3]
        self.sol.rotate_1(nums,k)
        self.assertEqual(nums, correctSolution, 'The result is incorrect on simple case.')

if __name__ == '__main__':
    unittest.main()