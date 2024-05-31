# LeetCode 88 - Merge Sorted Array
class Solution:
    def merge(nums1, m, nums2, n):
        # If one of the lists are empty, return the other.
        if m == 0:
            return nums2
        if n == 0:
            return nums1
        # Pointers for each list.
        x = m-1
        y = n-1
        z = m+n-1
        while z >= 0:
            # If done iterating the first list. Pull the rest from the second list.
            if x == -1:
                nums1[z] = nums2[y]
                y -= 1
                z -= 1
                continue
            # If done iterating the second list, the first list is good as is.
            if y == -1:
                break
            # Pull the larger value of the two lists at their current pointer.
            if nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1
            z -= 1
        return nums1