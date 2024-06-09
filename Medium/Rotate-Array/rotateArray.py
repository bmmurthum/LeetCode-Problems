class Solution:
    # My solution
    def rotate_1(self, nums: list[int], k: int) -> None:
        '''
        Rotates `nums` list `k` integers to the right. `k` is expected to be a non-negative integer.
        '''

        # Handling simple cases
        if len(nums) == 1:
            return
        if len(nums) == k:
            return
        if k == 0:
            return
        
        # Hold first value
        holder1 = nums[0]
        # Index of current position
        j = 0
        # Index of the value we started at
        start = 0
        for i in range(len(nums)):
            # Hold next value, to replace
            holder2 = nums[(k+j) % len(nums)]
            # Replace next value with first value
            nums[(k+j) % len(nums)] = holder1
            # Switch this new value to "first value" holding
            holder1 = holder2
            # If at end of loop and next-spot has been visited, move one space to right, and keep going.
            if (k+j) >= len(nums) and (k+j) % len(nums) == start:
                start += 1
                j = ((k+j) % len(nums)) + 1
                holder1 = nums[j]
            # Next spot is "k" items to the right.
            else:
                j = (k+j) % len(nums)

    # # Solution 2 - Someone else's solution
    # def rotate_2(self, nums: list[int], k: int) -> None:
    #     l = len(nums)
    #     k = k % l
    #     if k == 0:
    #         return
    #     nums[ :k], nums[k: ] = nums[l-k: ], nums[ :l-k]
    #     return
    
    # # Solution 3 - Someone else's solution
    # def rotate_3(self, nums: list[int], k: int) -> None:
    #     k = k % len(nums)
    #     rotated=nums[len(nums)-k:]+nums[:len(nums)-k]
    #     for i,number in enumerate(rotated):
    #         nums[i]=number
        
