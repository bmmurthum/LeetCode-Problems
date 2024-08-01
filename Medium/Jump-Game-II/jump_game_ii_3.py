class Solution:
    def jump_3(self, nums: list[int]) -> int:
        count = 0
        current = len(nums) - 1
        while current != 0:
            for i, n in enumerate(nums):
                if i + n >= current:
                    count += 1
                    current = i
                    break
        return count
