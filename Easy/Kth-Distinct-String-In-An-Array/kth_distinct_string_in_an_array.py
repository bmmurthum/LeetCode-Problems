"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def kth_distinct(self, arr: list[str], k: int) -> str:
        """
        Find a list of distinct strings within the given list. Return the kth distinct string found.

        Args:
            `arr`: The given array of strings.
            `k`: The item number we're looking for in the distinct list.
        Returns:
            `item`: The distinct string searched for.
        """

        # Look at all values to see if any are seen more than once.
        seen = set()
        distinct = set()
        for item in arr:
            if item not in seen:
                seen.add(item)
                distinct.add(item)
            elif item in distinct:
                distinct.remove(item)

        # If the output value doesn't exist, stop now.
        if len(distinct) < k:
            return ""

        # Iterate through the list to look for the kth distinct item.
        count = 1
        for _, item in enumerate(arr):
            if item in distinct:
                if k == count:
                    return item
                else:
                    count += 1
        return ""
