class Solution:
    def can_jump_3(self, nums: list[int]) -> bool:
        farthest = 0
        for num in nums:
            if farthest < 0:
                return False
            elif farthest < num:
                farthest = num
            farthest -= 1
        return True
