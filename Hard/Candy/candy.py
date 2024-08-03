""" Module to find minimum number of candies to give out. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201
# Ignore the advise to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem by LeetCode.com"""

    def candy(self, ratings: list[int]) -> int:
        """
        Return the minimum amount of candy to give to a group of kids. You must
        give more candy to a kid than their neighbor that has a lower rating.

        Args:
            `ratings`: The goodness rating of this child.
        Returns:
            `total_candies`: The minimum number of candies given out.
        """

        # Handle small cases
        length = len(ratings)
        if length == 1:
            return 1
        if length == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3

        # A list of candy to give to children
        candies_to_give = [-1] * length

        # Find all local minimums
        local_minimums = []
        for i in range(length):
            # Look at neighbors
            left_is_larger = False
            right_is_larger = False
            if i != 0 and ratings[i - 1] > ratings[i]:
                left_is_larger = True
            if i != length - 1 and ratings[i + 1] > ratings[i]:
                right_is_larger = True
            left_is_smaller = False
            right_is_smaller = False
            if i != 0 and ratings[i - 1] < ratings[i]:
                left_is_smaller = True
            if i != length - 1 and ratings[i + 1] < ratings[i]:
                right_is_smaller = True
            # Note as a minimum
            if (left_is_larger or right_is_larger) and not (
                left_is_smaller or right_is_smaller
            ):
                local_minimums.append(i)
                candies_to_give[i] = 1
                continue
            # If flat, note as one candy
            if not (
                left_is_larger or right_is_larger or left_is_smaller or right_is_smaller
            ):
                candies_to_give[i] = 1

        # Start iterations over the main list from various local_min.
        for local_min in local_minimums:

            # Look at neighbors
            left_is_larger = False
            right_is_larger = False
            if local_min != 0 and ratings[local_min - 1] > ratings[local_min]:
                left_is_larger = True
            if local_min != length - 1 and ratings[local_min + 1] > ratings[local_min]:
                right_is_larger = True

            # Go left from local_min
            if left_is_larger:
                last_amount = 1
                for i in range(local_min - 1, -1, -1):
                    right_is_smaller = ratings[i + 1] < ratings[i]
                    if right_is_smaller:
                        # If this spot has yet to be noted
                        if candies_to_give[i] == -1:
                            candies_to_give[i] = last_amount + 1
                        # If this spot has been seen
                        elif last_amount + 1 > candies_to_give[i]:
                            candies_to_give[i] = last_amount + 1
                            break
                        else:
                            break
                        last_amount += 1
                    else:
                        break

            # Go right from local_min
            if right_is_larger:
                last_amount = 1
                for i in range(local_min + 1, length):
                    left_is_smaller = ratings[i - 1] < ratings[i]
                    if left_is_smaller:
                        candies_to_give[i] = last_amount + 1
                        last_amount += 1
                    else:
                        break

        # Return the total candy given out
        return sum(candies_to_give)
