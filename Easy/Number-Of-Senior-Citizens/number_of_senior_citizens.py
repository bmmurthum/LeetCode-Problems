class Solution:
    """Problem given by LeetCode.com"""

    def count_seniors(self, details: list[str]) -> int:
        """
        Given a list of encoded details about passengers, get the number of
        passengers that are seniors.

        Args:
            `details`: A list of encoded passenger information.
        Returns:
            `count`: A count of senior passengers.
        """
        count = 0
        for info in details:
            if int(info[11:13]) > 60:
                count += 1
        return count


# a = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
a = ["1313579440F2036", "2921522980M5644"]
result = Solution().count_seniors(a)
print(f"Result: {result}")
