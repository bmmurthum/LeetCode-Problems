import unittest
from MergeSortedArray import Solution

class TestMergeSortedArray(unittest.TestCase):

    # Testing general case.
    def test_1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [1,2,2,3,5,6]
        self.assertEqual(x, correctSolution, 'The merge is incorrect')

    # Testing minimal case of one item and none in other.
    def test_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [1]
        self.assertEqual(x, correctSolution, 'The merge is incorrect. On empty second list.')

    # Testing minimal case of one item and none in other.
    def test_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [1]
        self.assertEqual(x, correctSolution, 'The merge is incorrect. On empty first list.')

    # Tests a larger case of a full second list and empty first list.
    def test_4(self):
        nums1 = [0,0,0,0,0,0,0]
        m = 0
        nums2 = [1,3,3,4,5,6,10]
        n = 7
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [1,3,3,4,5,6,10]
        self.assertEqual(x, correctSolution, 'The merge is incorrect. On empty first list.')

    # Tests a larger case of a full first list and empty second list.
    def test_5(self):
        nums1 = [1,2,3,4,4,4,5,6,6,7]
        m = 10
        nums2 = []
        n = 0
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [1,2,3,4,4,4,5,6,6,7]
        self.assertEqual(x, correctSolution, 'The merge is incorrect. On empty second list.')

    # Tests negative number
    # Tests second list being smaller and having values on both sides of solution.
    def test_6(self):
        nums1 = [1,2,3,4,4,4,5,6,6,7,0,0,0,0]
        m = 10
        nums2 = [-1,3,3,8]
        n = 4
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [-1,1,2,3,3,3,4,4,4,5,6,6,7,8]
        self.assertEqual(x, correctSolution, 'The merge is incorrect.')

    # Testing all negative numbers.
    def test_7(self):
        nums1 = [-8,-5,-3,-3,-2,0,0,0,0]
        m = 5
        nums2 = [-7,-4,-4,-1]
        n = 4
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [-8,-7,-5,-4,-4,-3,-3,-2,-1]
        self.assertEqual(x, correctSolution, 'The merge is incorrect. On all negatives list.')

    # Testing some zeroes.
    def test_8(self):
        nums1 = [-1,0,0,0,2,4,0,0,0,0]
        m = 6
        nums2 = [1,1,2,5]
        n = 4
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [-1,0,0,0,1,1,2,2,4,5]
        self.assertEqual(x, correctSolution, 'The merge is incorrect. On some zeroes list.')

    # Testing all zeroes.
    def test_9(self):
        nums1 = [0,0,0,0,0,0,0,0]
        m = 5
        nums2 = [0,0,0]
        n = 3
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [0,0,0,0,0,0,0,0]
        self.assertEqual(x, correctSolution, 'The merge is incorrect. On all zeroes list.')

    # Testing first list being all larger values.
    def test_10(self):
        nums1 = [11,13,13,20,0,0]
        m = 4
        nums2 = [3,4]
        n = 2
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [3,4,11,13,13,20]
        self.assertEqual(x, correctSolution, 'The merge is incorrect.')

    # Testing second list being all larger values.
    def test_11(self):
        nums1 = [1,2,2,0,0,0,0,0]
        m = 3
        nums2 = [10,11,12,14,14]
        n = 5
        x = Solution.merge(nums1,m,nums2,n)
        correctSolution = [1,2,2,10,11,12,14,14]
        self.assertEqual(x, correctSolution, 'The merge is incorrect.')


if __name__ == '__main__':
    unittest.main()