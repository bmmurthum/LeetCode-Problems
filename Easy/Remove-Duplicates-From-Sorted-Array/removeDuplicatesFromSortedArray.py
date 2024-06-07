class Solution:
    def removeDuplicates_1(self, nums: list[int]) -> int:
        """
        Removes duplicates from a sorted list of non-descending integers.
        Args:
            `nums` (list[int]): A sorted list of non-descending integers.
        Returns:
            `int`: The length of the list after removing duplicates.
        This function iterates through the list of integers and "removes" duplicates. The initial list is changed by reference and the returned `int` represents the new end of this list, with garbage values after. 
        """
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