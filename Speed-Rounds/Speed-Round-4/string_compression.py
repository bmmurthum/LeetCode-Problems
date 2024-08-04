class Solution:
    """Problem provided by LeetCode"""

    def compress(self, chars: list[str]) -> int:
        """
        Compresses a list of letters to a different format. The compressed
        version is stored in-place inside `chars`.

        Args:
            `chars`: A list of characters
        Returns:
            `new_index_ptr`: The length of the new compressed "string."
        """

        # 19 min

        # Handle single item case
        if len(chars) == 1:
            return 1

        count = 1
        letter = chars[0]
        new_index_ptr = 0
        for i in range(1, len(chars)):
            if chars[i] == letter:
                count += 1
            # If different than current letter
            # Add current letter to output
            else:
                chars[new_index_ptr] = letter
                letter = chars[i]
                new_index_ptr += 1
                if count > 1:
                    count_string = str(count)
                    for char in count_string:
                        chars[new_index_ptr] = char
                        new_index_ptr += 1
                count = 1

        # On reaching the end of list
        chars[new_index_ptr] = letter
        new_index_ptr += 1
        if count > 1:
            count_string = str(count)
            for char in count_string:
                chars[new_index_ptr] = char
                new_index_ptr += 1

        # Returns the length of the changes values.
        return new_index_ptr
