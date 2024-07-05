class Solution:
    def majority_element_3(self, nums: list[int]) -> int:
        counter, majority = 1, nums[0]
        for num in nums[1:]:
            if num == majority:
                counter += 1
            else:
                counter -= 1
            if not counter:
                majority = num
                counter += 1
        return majority
