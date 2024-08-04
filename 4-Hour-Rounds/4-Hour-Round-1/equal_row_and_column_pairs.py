"""Problem from LeetCode.com"""

# Ignore the advice to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def equal_pairs(self, grid: list[list[int]]) -> int:
        """
        Return a count of how many match col/row pairs you can find.

        Args:
            `grid`: A 2D array of integers
        Returns:
            `count`: A quantity of matching col/row pairs.
        """

        # Build a dict of hashes of the row values, and their count.
        row_hashes = {}
        for _, row in enumerate(grid):
            curr_hash = hash(str(row))
            if curr_hash not in row_hashes:
                row_hashes[curr_hash] = 1
            else:
                row_hashes[curr_hash] += 1

        # Count number of columns that are in the hash list of rows.
        total_matches = 0
        for x in range(len(grid)):
            col = []
            for y in range(len(grid)):
                col.append(grid[y][x])
            col_hash = hash(str(col))
            if col_hash in row_hashes:
                total_matches += row_hashes[col_hash]
        return total_matches


# Correct = 1
a = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

# Correct = 3
# a = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
result = Solution().equal_pairs(a)
print(f"Result: {result}")
