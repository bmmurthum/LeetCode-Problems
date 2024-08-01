class Solution:
    def jump_2(self, nums: list[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(nums) - 1:
            farthest = 0
            for x in range(l, r + 1):
                farthest = max(farthest, x + nums[x])
            l = r + 1
            r = farthest
            res += 1
        return res
