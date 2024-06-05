import unittest
from minStack import MinStack

class testing(unittest.TestCase):

    # Testing simple case. No pop().
    def test_1(self):
        obj = MinStack()
        testList = [-1,-2,2,3,-2]
        for x in testList:
            obj.push(x)
        result = (obj.top(),obj.getMin())
        correctSolution = (-2,-2)
        self.assertEqual(result, correctSolution, 'The result is incorrect on simple case.')
        
    # Testing all zero case.
    def test_2(self):
        obj = MinStack()
        testList = [0,0,0]
        for x in testList:
            obj.push(x)
        result = (obj.top(),obj.getMin())
        correctSolution = (0,0)
        self.assertEqual(result, correctSolution, 'The result is incorrect on simple case.')

    # Testing minimum at the end.
    def test_3(self):
        obj = MinStack()
        testList = [0,0,0,-1]
        for x in testList:
            obj.push(x)
        result = (obj.top(),obj.getMin())
        correctSolution = (-1,-1)
        self.assertEqual(result, correctSolution, 'The result is incorrect on simple case.')

    # Testing minimum not at end.
    def test_4(self):
        obj = MinStack()
        testList = [0,0,0,-1,0]
        for x in testList:
            obj.push(x)
        result = (obj.top(),obj.getMin())
        correctSolution = (0,-1)
        self.assertEqual(result, correctSolution, 'The result is incorrect on simple case.')

    # Testing simple case with pop.
    def test_5(self):
        obj = MinStack()
        testList = [0,0,0,-1,0]
        for x in testList:
            obj.push(x)
        obj.pop()
        result = (obj.top(),obj.getMin())
        correctSolution = (-1,-1)
        self.assertEqual(result, correctSolution, 'The result is incorrect on simple case.')

    # Testing minimum in beginning with multiple pop().
    def test_6(self):
        obj = MinStack()
        testList = [-7,1,-4,3,4]
        for x in testList:
            obj.push(x)
        obj.pop()
        obj.pop()
        obj.pop()
        result = (obj.top(),obj.getMin())
        correctSolution = (1,-7)
        self.assertEqual(result, correctSolution, 'The result is incorrect on simple case.')

    # Testing descending order, minimum always at end. No pop().
    def test_7(self):
        obj = MinStack()
        testList = [-1,-2,-3,-4,-5]
        for x in testList:
            obj.push(x)
        result = (obj.top(),obj.getMin())
        correctSolution = (-5,-5)
        self.assertEqual(result, correctSolution, 'Descending order of push()')

    # Testing descending order, minimum always at end. Two pop().
    def test_8(self):
        obj = MinStack()
        testList = [-1,-2,-3,-4,-5]
        for x in testList:
            obj.push(x)
        obj.pop()
        obj.pop()
        result = (obj.top(),obj.getMin())
        correctSolution = (-3,-3)
        self.assertEqual(result, correctSolution, 'Descending order of push(). Two pop().')

    # Testing ascending order, minimum always at beginning. No pop().
    def test_9(self):
        obj = MinStack()
        testList = [1,2,3,4,5]
        for x in testList:
            obj.push(x)
        result = (obj.top(),obj.getMin())
        correctSolution = (5,1)
        self.assertEqual(result, correctSolution, 'Ascending order of push()')

    # Testing ascending order, minimum always at beginning. Two pop().
    def test_10(self):
        obj = MinStack()
        testList = [1,2,3,4,5]
        for x in testList:
            obj.push(x)
        obj.pop()
        obj.pop()
        result = (obj.top(),obj.getMin())
        correctSolution = (3,1)
        self.assertEqual(result, correctSolution, 'Ascending order of push(). Two pop().')

    # Testing pop() down to one value in the stack.
    def test_11(self):
        obj = MinStack()
        testList = [1,2,3,4,5]
        for x in testList:
            obj.push(x)
        obj.pop()
        obj.pop()
        obj.pop()
        obj.pop()
        result = (obj.top(),obj.getMin())
        correctSolution = (1,1)
        self.assertEqual(result, correctSolution, 'Pop() down to one value.')

    # Testing pop all values. Add two back.
    def test_12(self):
        obj = MinStack()
        testList = [1,2,3,4,5]
        for x in testList:
            obj.push(x)
        obj.pop()
        obj.pop()
        obj.pop()
        obj.pop()
        obj.pop()
        obj.push(1)
        obj.push(4)
        result = (obj.top(),obj.getMin())
        correctSolution = (4,1)
        self.assertEqual(result, correctSolution, 'Pop() down to one value.')

if __name__ == '__main__':
    unittest.main()