"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        """
        Find the length of the longest shared subsequence.

        Ex: text1 = "abcde", text2 = "acfe", shared = "ace", len == 3

        Args:
            `text1`: A first string.
            `text2`: A second string.
        Returns:
            `output`: The length of the longest shared subsequence.
        """

        # Initialize a grid with all zeroes.
        grid = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        found = 0
        for i in range(len(grid[0])):
            if text1[i] == text2[0]:
                found = 1
            grid[0][i] = found
        found = 0
        for j in range(len(grid)):
            if text2[j] == text1[0]:
                found = 1
            grid[j][0] = found

        # Starting at [1,1] generate the board with calculations based on the
        # neighbors to the top, left and top-left and whether this character is
        # matched between the two strings.
        for x in range(1, len(grid[0])):
            for y in range(1, len(grid)):
                if text1[x] == text2[y]:
                    grid[y][x] = grid[y - 1][x - 1] + 1
                else:
                    grid[y][x] = max(grid[y - 1][x], grid[y][x - 1])

        # Return the value of the bottom right corner.
        output = grid[len(grid) - 1][len(grid[0]) - 1]
        return output
