# Testing

A selection of code coverage and testing methods.

### Unit Tests

Using Python's `unittest` library we can test a variety of inputs on our methods. For quality assurance.

```python
import unittest
from evaluateReversePolistNotation import Solution

class testing(unittest.TestCase):
  # Testing simple case.
  def test_1(self):
    s = Solution()
    tokens = ["2","1","+","3","*"]
    correctSolution = 9
    result = s.evalRPN(tokens)
    self.assertEqual(result, correctSolution, 'The result is incorrect.')
```

### Memory Tracing

With [memory tracing](https://www.geeksforgeeks.org/monitoring-memory-usage-of-a-running-python-program/#) we can consider optimizing for memory and checking for memory leaks.

With `tracemalloc`:

```python
import tracemalloc

def app():
  lt = []
  for i in range(0, 100000):
      lt.append(i)

# starting the monitoring
tracemalloc.start()

# function call
app()

# displaying the memory
print(tracemalloc.get_traced_memory())

# stopping the library
tracemalloc.stop()
```

With `memory_profiler`:

```
pip install memory_profiler
python -m memory_profiler your_code.py
```

```
Filename: your_code.py

Line #    Mem usage    Increment   Line Contents
================================================
     4   21.289 MiB    0.000 MiB   @profile
     5                             def so_slow(bar):
     6   21.289 MiB    0.000 MiB       sleep(5)
     7   21.289 MiB    0.000 MiB       return bar
```

### Performance

With `timeit` we can isolate a section of code to run hundreds of times to get an idea for run-time differences with alterations.

```python
import timeit
numTests = 100
mycode = '''
class Solution:
    def removeDuplicates_1(self, nums: list[int]) -> int:
        ptr = 1
        lastValue = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != lastValue:
                nums[ptr] = nums[i]
                lastValue = nums[i]
                ptr += 1
        return ptr
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
v = s.removeDuplicates_1(nums)
'''
timePerRun = str(timeit.timeit(stmt=mycode,number=numTests)/numTests)
print("removeDuplicates():" + timePerRun)
```

A Stack Overflow [user](https://stackoverflow.com/questions/44677606/how-to-measure-the-speed-of-a-python-function) suggests using `line_profiler` to see a line-by-line diagnostic. 

```
pip install line_profiler
```

```python
from time import sleep

@profile
def so_slow(bar):
  sleep(5)
  return bar

if __name__ == "__main__":
    so_slow(5)
```

```
kernprof -l -v your_code.py
```

```
Wrote profile results to your_code.py.lprof
Timer unit: 1e-06 s

Total time: 5.00283 s
File: your_code.py
Function: so_slow at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def so_slow(bar):
     6         1      5002830 5002830.0    100.0      sleep(5)
     7         1            2      2.0      0.0      return bar
```





