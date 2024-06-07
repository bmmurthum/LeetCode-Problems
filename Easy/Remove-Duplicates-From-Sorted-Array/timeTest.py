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


mycode = '''
class Solution:
    def removeDuplicates_2(self, nums: list[int]) -> int:
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
v = s.removeDuplicates_2(nums)
'''
timePerRun = str(timeit.timeit(stmt=mycode,number=numTests)/numTests)
print("removeDuplicates_2():" + timePerRun)


mycode = '''
class Solution:
    def removeDuplicates_3(self, nums: list[int]) -> int:
        setNums = set(nums)
        setNums = sorted(setNums)
        j = 0
        for i in setNums:
            nums[j] = i
            j = j + 1
        return j
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
v = s.removeDuplicates_3(nums)
'''
timePerRun = str(timeit.timeit(stmt=mycode,number=numTests)/numTests)
print("removeDuplicates_3():" + timePerRun)


mycode = '''
class Solution:
    def removeDuplicates_4(self, nums: list[int]) -> int:
        setNums = list(set(nums))
        nums.clear()
        nums.extend(setNums)
        return len(nums)
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
v = s.removeDuplicates_4(nums)
'''
timePerRun = str(timeit.timeit(stmt=mycode,number=numTests)/numTests)
print("removeDuplicates_4():" + timePerRun)