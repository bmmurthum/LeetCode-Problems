class Solution:
    def longest_consecutive_3(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        longest = 0
        length = 0
        prev = -1
        for num in nums:
            if prev + 1 == num:
                length += 1
            else:
                if length > longest:
                    longest = length
                length = 1
            prev = num
        if length > longest:
            longest = length
        return longest
