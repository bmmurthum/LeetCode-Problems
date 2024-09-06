"""Problem from LeetCode.com"""

# pylint: disable=C0200

import math


class Solution:
    """Problem from LeetCode.com"""

    def successful_pairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        """
        Given a list of `spells` where each int element is the "strength" of
        the spell, and given a list of `potions` in the same way, a successful
        combination of a spell and potion is defined as if the value of the
        spell multiplied by the value of the potion is above or equal to
        `success`.

        For each spell, we want to know how many successful combinations are
        possible. Return a generated list of size `len(spells)` with these
        values.

        Args:
            `spells`: A list of spell strengths.
            `potions`: A list of potion strengths.
            `success`: A desired target strength for each combination.
        Returns:
            `output`: A list of success counts for each spell.
        """

        # For each spell, we know that there's a minimum strength of potion
        # that's needed to find a success. We do a binary search on the sorted
        # potions list to find an index that is at the limit between above/
        # equal and below this value. In the case of multiple matching values,
        # we may need to move left some steps.
        potions.sort()
        output = []
        for spell in spells:

            # Find a target minimum value to look for.
            target_potion_value = math.ceil(success / spell)

            # If all potions meet our desired strength.
            if potions[0] >= target_potion_value:
                output.append(len(potions))
                continue

            # If no potions meet our desired strength.
            if potions[-1] < target_potion_value:
                output.append(0)
                continue

            # Binary search for the index for a desired strength.
            i = len(potions) // 2
            move_length = i // 2
            while move_length > 0:
                if potions[i] < target_potion_value:
                    i += move_length
                elif potions[i] > target_potion_value:
                    i -= move_length
                elif (
                    potions[i] == target_potion_value
                    and potions[i - 1] == target_potion_value
                ):
                    i -= move_length
                move_length = move_length // 2

            # Shift left/right until on top of desired strength.
            # Fixing off-by-ones from binary positioning.
            if potions[i] >= target_potion_value:
                while potions[i - 1] >= target_potion_value:
                    i -= 1
            if potions[i] < target_potion_value:
                while potions[i] < target_potion_value:
                    i += 1

            # Apply and move to next spell.
            output.append(len(potions) - i)

        return output
