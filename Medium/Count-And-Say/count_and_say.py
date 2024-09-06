"""Problem from LeetCode.com"""

import sys


# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def count_and_say(self, n: int) -> str:
        """
        Performs a run-length-encoding on a starting number "1". To then feed
        that output into itself `n` times. We find the nth output.

        Args:
            `n`: How many times to run the internal iterations.
        Returns:
            `output`: The generated string of integers.
        """

        sys.set_int_max_str_digits(0)

        def helper(given: int) -> int:
            """
            Perform a run-length-encoding on an integer to then output that as
            integer to allow for taking its output as the next input.

            Args:
                `given`: The given integer to encode.
            Returns:
                `output`: The encoded integer.
            """

            # "1111" -> "41"
            # "41" -> "1411"
            # "1411" -> "111421"

            b = str(given)
            output = ""
            current_num = b[0]
            count = 1
            for i in range(1, len(b)):
                if b[i] == current_num:
                    count += 1
                else:
                    output += str(count)
                    output += current_num
                    count = 1
                    current_num = b[i]
            output += str(count)
            output += current_num
            return int(output)

        # Edge-case
        if n == 1:
            return "1"

        # Run the cycles, starting at second iteration.
        output = 11
        i = 2
        while i < n:
            output = helper(output)
            i += 1
        return str(output)
