"""Problem from LeetCode.com"""

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
#
#   1 <= piles.length <= 10^4
#   piles.length <= h <= 10^9
#   1 <= piles[i] <= 10^9
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

import math


class Solution:
    """Problem from LeetCode.com"""

    def min_eating_speed(self, piles: list[int], h: int) -> int:
        """
        Finds a minimum `k` such that Koko will eat at most this many bananas
        from a pile in an hour and still eats all bananas before the guards
        return in `h` hours. piles[i] is how many bananas are in a single pile.

        Args:
            `piles`: A list of bananas piles.
            `h`: How many hours before the guards return.
        Returns:
            `k`: A max number of bananas eaten per hour. (As low as possible.)
        """

        def can_eat_all_bananas(piles: list[int], h: int, k: int) -> bool:
            """
            Iterates through piles list to see if by eating k bananas per hour
            we can finish all the piles before h hours.

            Args:
                `piles`: A list of bananas piles.
                `h`: How many hours before the guards return.
                `k`: A number of bananas eaten per hour.
            Returns:
                `True/False`: Whether possible.
            """

            hours_used = 0
            for pile in piles:
                hours_used += math.ceil(pile / k)
                if hours_used > h:
                    return False
            if hours_used > h:
                return False
            else:
                return True

        # Edge-case. One pile.
        if len(piles) == 1:
            return math.ceil(piles[0] / h)

        # Edge-case: h == len(piles)
        if h == len(piles):
            return max(piles)

        # We know a total number of bananas is the sum(piles). This divided by
        # some h is an absolute minimum of banana-eating, regardless of
        # pile-behavior. This can be a minimum search value.
        # Ex: piles = [3, 6, 7, 11], h = 9,
        #     sum(piles) == 27
        #     min_rate == math.ceil(27 / 9) == 3

        # A maximum search value can be the max(piles) because this would allow
        # a pile per hour and h is guaranteed to be equal or above len(piles).
        # Ex: piles = [3, 6, 7, 11], h = 9,
        #     max_rate == max(piles) == 11

        # A smaller maximum search value can be determined by the following.
        # len(piles) / h : is a number of rate of how many piles per hour need
        # to be taken. We can guarantee this rate if we eat close to
        # (len(piles) / h) of max(piles). We also need to account for h being
        # divisible by len(piles). We'll divided by the closest number below h
        # that is divisible by len(piles).
        # Ex: piles = [3, 6, 7, 11], h = 9,
        #     len(piles) == 4, max(piles) == 11
        #     h - (h % len(piles)) == 8
        #     max_rate == math.ceil(11 * (4 / 8)) == math.ceil(5.5) == 6

        # We can iterate through the piles list with a number of guesses equal
        # to log2(len(piles)) times by using a binary search to find new
        # guesses. This allows us to avoid sorting the array. The max length of
        # piles is 10^9, log2(10^9) == 30. 30 max iterations over the list.

        # We can stop iterating through the list early if we reach h in
        # eating-periods. If we sort starting from max-value, this h may be
        # reached faster. We'd only need to sort once, while iterations my be
        # close to 30. List sort every time forces a best case at O(n log n),
        # when it could be faster without the sort.
        # piles.sort(reverse=True)

        min_rate = math.ceil(sum(piles) / h)
        max_rate = math.ceil(max(piles) * (len(piles) / (h - (h % len(piles)))))

        # Edge-Case: Our initial edges are a successful output.
        if min_rate == max_rate:
            return min_rate

        # Binary search down to last two options.
        while min_rate + 1 < max_rate:
            mid = (min_rate + max_rate) // 2
            if can_eat_all_bananas(piles, h, mid):
                max_rate = mid
            else:
                min_rate = mid
        if can_eat_all_bananas(piles, h, min_rate):
            return min_rate
        else:
            return max_rate
