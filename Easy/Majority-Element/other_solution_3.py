class Solution:
    def majority_element_4(self, nums: list[int]) -> int:
        count = 0
        res = 0
        for i in nums:
            if count != 0:
                if res != i:
                    count -= 1
                else:
                    count += 1
            else:
                if res == i:
                    count += 1
                else:
                    res = i
                    count += 1
        return res
