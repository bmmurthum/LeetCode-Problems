class Solution:
    """Problem provided by LeetCode"""

    def convert(self, s: str, num_rows: int) -> str:
        """
        Converts a string to a mixed string based on a zigzagging pattern.

        Args:
            `s`: A given string to change.
            `num_rows`: The rows of the zigzag.
        Return:
            `final_string`: The newly changed string.
        """

        # 13 min

        # Fixes:
        # - Fixed error in not applying enumerate(row_holder)

        # Edge cases
        if len(s) < 3:
            return s
        if num_rows == 1:
            return s

        # A list for each row
        row_holder = []
        for _ in range(num_rows):
            row_holder.append([])

        # Add letters to row lists
        ascending = True
        current_row = 0
        for letter in s:
            # Add letter to its list
            row_holder[current_row].append(letter)
            # Should we switch directions?
            if current_row == 0:
                ascending = True
            elif current_row == num_rows - 1:
                ascending = False
            # Apply step
            if ascending:
                current_row += 1
            else:
                current_row -= 1

        # Build and return string
        final_string = ""
        for _, row in enumerate(row_holder):
            for letter in row:
                final_string += letter
        return final_string
