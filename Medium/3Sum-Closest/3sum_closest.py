"""Problem from LeetCode.com"""

# pylint: disable=C0200
# pylint: disable=C0103


class Solution:
    """Problem from LeetCode.com"""

    def three_sum_closest(self, nums: list[int], target: int) -> int:
        """
        Find a case of three numbers in `nums` that have a sum as close as
        possible to the `target` value. Return the closest sum found. The input
        cases guarantee that there is only one closest.

        Args:
            `nums`: A list of negative/positive integers.
            `target`: A target sum to attempt to find.
        Returns:
             `closest_sum`: A closest sum of three integers.
        """

        # Handle edge-case.
        if len(nums) == 3:
            return sum(nums)

        # Initial set up.
        nums.sort()
        left_ptr = 0
        right_ptr = len(nums) - 1
        closest_sum = sum([nums[0], nums[-1], nums[-2]])
        closest_dist = abs(target - closest_sum)

        # Handle edge-case.
        # If target is above or below the possible max/min sums.
        highest_possible = sum([nums[-1], nums[-2], nums[-3]])
        if target > highest_possible:
            return highest_possible
        lowest_possible = sum([nums[0], nums[1], nums[2]])
        if target < lowest_possible:
            return lowest_possible

        # Combination two-pointers, shrinking window, expanding search.
        for left_ptr in range(0, len(nums) - 2):
            area = set(nums[left_ptr + 2 :])
            for right_ptr in range(left_ptr + 1, len(nums) - 1):

                # Consider shrinking the area-set.
                # If the number after the one we're about to move into is
                # different, take our current number out from the set.
                if nums[right_ptr + 1] != nums[right_ptr] and nums[right_ptr] in area:
                    area.remove(nums[right_ptr])

                # Our desired find for perfect match.
                search = target - (nums[left_ptr] + nums[right_ptr])

                # Expand this number outward to find a closest match.
                # Stop expanding at the current closest match distance.
                if search in area:
                    return target
                search_small = search
                search_large = search

                # If the target is well above any values in the set, don't
                # search. Same for well below.
                val_max_area = max(area)
                val_min_area = min(area)
                best_guess_max = nums[left_ptr] + nums[right_ptr] + val_max_area
                best_guess_min = nums[left_ptr] + nums[right_ptr] + val_min_area
                if (
                    target > val_max_area
                    and abs(target - best_guess_max) > closest_dist
                ):
                    continue
                if (
                    target < val_min_area
                    and abs(target - best_guess_min) > closest_dist
                ):
                    continue

                # Do a search for closest target value in the set.
                for i in range(1, closest_dist):
                    search_small -= 1
                    search_large += 1
                    if search_small in area:
                        closest_dist = i
                        closest_sum = target - i
                        break
                    if search_large in area:
                        closest_dist = i
                        closest_sum = target + i
                        break

        return closest_sum
