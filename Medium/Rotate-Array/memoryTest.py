import tracemalloc

class Solution:
    # My solution
    def rotate_1(self, nums: list[int], k: int) -> None:
        if len(nums) == 1:
            return
        if len(nums) == k:
            return
        if k == 0:
            return
        holder1 = nums[0]
        j = 0
        start = 0
        for i in range(len(nums)):
            holder2 = nums[(k+j) % len(nums)]
            nums[(k+j) % len(nums)] = holder1
            holder1 = holder2
            if (k+j) >= len(nums) and (k+j) % len(nums) == start:
                start += 1
                j = ((k+j) % len(nums)) + 1
                holder1 = nums[j]
            else:
                j = (k+j) % len(nums)
    # Solution 2 - Someone else's solution
    def rotate_2(self, nums: list[int], k: int) -> None:
        l = len(nums)
        k = k % l
        if k == 0:
            return
        nums[ :k], nums[k: ] = nums[l-k: ], nums[ :l-k]
        return
    # Solution 3 - Someone else's solution
    def rotate_3(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        rotated=nums[len(nums)-k:]+nums[:len(nums)-k]
        for i,number in enumerate(rotated):
            nums[i]=number


# Testing Memory Allocation
# rotate_1()
nums = [1,2,3,4,5,6,7,8,9,10]
k = 6
tracemalloc.start()
s = Solution()
v = s.rotate_1(nums,k)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("rotate_1(): " + tracedMemoryPeak + " blocks")


# Testing Memory Allocation
# rotate_2()
nums = [1,2,3,4,5,6,7,8,9,10]
k = 6
tracemalloc.start()
s = Solution()
v = s.rotate_2(nums,k)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("rotate_2(): " + tracedMemoryPeak + " blocks")


# Testing Memory Allocation
# rotate_3()
nums = [1,2,3,4,5,6,7,8,9,10]
k = 6
tracemalloc.start()
s = Solution()
v = s.rotate_3(nums,k)
tracedMemoryPeak = str(tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
print("rotate_3(): " + tracedMemoryPeak + " blocks")