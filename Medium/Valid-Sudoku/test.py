import unittest
from validSudoku import Solution

class TestMergeSortedArray(unittest.TestCase):

    # Testing general case.
    def test_1(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        x = Solution.isValidSudoku(board)
        correctSolution = True
        self.assertEqual(x, correctSolution, 'Incorrect. This puzzle has no visible invalid pieces.')

    # Bad first column
    def test_2(self):
        board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        x = Solution.isValidSudoku(board)
        correctSolution = False
        self.assertEqual(x, correctSolution, 'Incorrect. This puzzle has a visible mistake.')

    # Bad first row
    def test_3(self):
        board = [["5","3",".",".","7",".","5",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        x = Solution.isValidSudoku(board)
        correctSolution = False
        self.assertEqual(x, correctSolution, 'Incorrect. This puzzle has a visible mistake.')

    # Bad sub-box
    def test_4(self):
        board = [["5","3",".",".","7",".","5",".","."],["6",".",".","1","9","5","6",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        x = Solution.isValidSudoku(board)
        correctSolution = False
        self.assertEqual(x, correctSolution, 'Incorrect. This puzzle has a visible mistake.')


if __name__ == '__main__':
    unittest.main()
