"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def minimum_pushes(self, word: str) -> int:
        """
        Imagining a phone keypad that you decide which letters go on which
        numbers, what's a minimum number of key presses you can press for a
        given word.

        Args:
            `word`: A given word to type.
        Returns:
            `minimum_presses`: A minimum number of finger presses to write the
                word.
        """

        # Count using a dictionary for hash-speed.
        # Then apply to a list to sort the counted values, highest to lowest.
        letter_counts = {}
        for letter in word:
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1
        sorted_letter_counts = []
        for item in letter_counts:
            sorted_letter_counts.append(letter_counts.get(item))
        sorted_letter_counts.sort(reverse=True)

        # Consider putting the highly pressed keys as first available.
        # Run as simulation, then return total presses.
        multiplier = 1
        count = 1
        total_presses = 0
        for value in sorted_letter_counts:
            total_presses += multiplier * value
            count += 1
            if count > 8:
                count = 1
                multiplier += 1
        return total_presses
