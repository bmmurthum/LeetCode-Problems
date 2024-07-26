class Solution:
    def summary_ranges_2(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ranges = []
        n = len(nums)
        i = 0
        while i < n:
            start = nums[i]
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            if j > i:
                ranges.append(f"{start}->{nums[j]}")
            else:
                ranges.append(str(start))
            i = j + 1
        return ranges
