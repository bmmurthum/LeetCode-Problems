import tracemalloc

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
    
    def removeDuplicates_2(self, nums: list[int]) -> int:
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count
    
    def removeDuplicates_3(self, nums: list[int]) -> int:
        setNums = set(nums)
        setNums = sorted(setNums)
        j = 0
        for i in setNums:
            nums[j] = i
            j = j + 1
        return j
    
    def removeDuplicates_4(self, nums: list[int]) -> int:
        setNums = list(set(nums))
        nums.clear()
        nums.extend(setNums)
        return len(nums)
    
    
# Testing Memory Allocation
# removeDuplicates_1()
nums = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6,7,8,9,10]
tracemalloc.start()
s = Solution()
v = s.removeDuplicates_1(nums)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("removeDuplicates_1(): " + tracedMemoryPeak + " blocks")


# removeDuplicates_2()
nums = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6,7,8,9,10]
tracemalloc.start()
s = Solution()
v = s.removeDuplicates_2(nums)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("removeDuplicates_2(): " + tracedMemoryPeak + " blocks")


# removeDuplicates_3()
nums = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6,7,8,9,10]
tracemalloc.start()
s = Solution()
v = s.removeDuplicates_3(nums)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("removeDuplicates_3(): " + tracedMemoryPeak + " blocks")


# removeDuplicates_4()
nums = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6,7,8,9,10]
tracemalloc.start()
s = Solution()
v = s.removeDuplicates_4(nums)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("removeDuplicates_4(): " + tracedMemoryPeak + " blocks")