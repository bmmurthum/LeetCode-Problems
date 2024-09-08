"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def letter_combinations(self, digits: str) -> list[str]:
        """
        Given a phone number represented by `digits`, return all the possible
        letter combinations that phone number could be represented as on a
        phone keyboard (an older phone).

        Args:
            `digits`: A string of integer digits representing a phone number.
        Returns:
            `output`: A list of strings of lower-case characters.
        """

        def recursive_pathing(current_built_string: str, depth: int) -> None:
            """
            Traverses depth-first to build a string as it goes deeper. Ending
            at the depth equal to the len(digits). Upon hitting the ending
            depth, appends the built string to an output list.

            Args:
                `current_built_string`: The current built string before adding
                    the current depth character.
                `depth`: The current depth.
            """

            for letter in keyboard[digits[depth]]:
                current_string = current_built_string + letter
                # If the next depth is the end, append answer to list.
                if depth + 1 == len(digits) - 1:
                    for next_letter in keyboard[digits[depth + 1]]:
                        output.append(current_string + next_letter)
                # Otherwise, continue.
                else:
                    recursive_pathing(current_string, depth + 1)

        # Helpers
        output = []
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Edge-case: Handle empty string.
        if len(digits) == 0:
            return []
        # Edge-case: Single digit in string.
        if len(digits) == 1:
            for letter in keyboard[digits[0]]:
                output.append(letter)
            return output

        # Do the recursion function that will append outputs to the list.
        recursive_pathing("", 0)

        # Return generated list.
        return output
