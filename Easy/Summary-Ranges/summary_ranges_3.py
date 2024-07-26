class Solution:
    def summary_ranges_3(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        result = []
        prev_num = nums[0]
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev_num + 1:
                prev_num = nums[i]
            else:
                if prev_num != start:
                    result.append(f"{start}->{prev_num}")
                else:
                    result.append(f"{start}")
                start = nums[i]
                prev_num = nums[i]
        if prev_num != start:
            result.append(f"{start}->{prev_num}")
        else:
            result.append(f"{start}")
        return result
