class Solution:
    """Problem provided by LeetCode"""

    def kids_with_candies(self, candies: list[int], extra_candies: int) -> list[bool]:
        """
        A group of kids each have a number of candies. This is held in
        `candies`. You hold a number of candies `extra_candies`. This method
        returns a list that is `True/False` if you gave all your candies to a
        kid, would they now have the most or equal to most.

        Args:
            `candies`: A list of how many candies each kid has.
            `extra_candies`: The number of candies you have.
        Returns:
            `now_has_max`: A boolean list of if the kid could now have max
            candy.
        """

        # 4 min 30 sec

        max_num_candies = max(candies)
        now_has_max = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extra_candies >= max_num_candies:
                now_has_max[i] = True
        return now_has_max
