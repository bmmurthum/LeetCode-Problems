class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pnt = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[pnt] = nums[i]
                pnt += 1
        # The LeetCode Test-Cases require you pop() from your list
        # even though it's requirements describe to not do this.
        # for j in range(0,len(nums)-pnt):
        #     nums.pop()
        return pnt