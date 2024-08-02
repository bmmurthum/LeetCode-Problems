""" Module to convert integer to roman numeral. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201
# Ignore the advise to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem by LeetCode.com"""

    def int_to_roman(self, num: int) -> str:
        """
        Converts a digit [1,3999] to roman numerals.

        Args:
            `num`: The integer format input.
        Returns:
            `output`: The string roman numeral version.
        """

        quick_vals = {
            1: "I",
            4: "IV",
            9: "IX",
            10: "X",
            40: "XL",
            90: "XC",
            100: "C",
            400: "CD",
            900: "CM",
            1000: "M",
            5: "V",
            50: "L",
            500: "D",
        }

        # Handle string building digit by digit.
        num_as_string = str(num)
        decimal = 1
        output = ""
        for i in range(len(num_as_string) - 1, -1, -1):
            value = int(num_as_string[i]) * decimal
            # Handle quick-knowns
            if value in quick_vals:
                output = quick_vals[value] + output
                decimal = decimal * 10
                continue
            # Handle additives
            temp_output = ""
            while value > 0:
                if value >= 1000:
                    temp_output += "M"
                    value -= 1000
                    continue
                elif value >= 500:
                    temp_output += "D"
                    value -= 500
                    continue
                elif value >= 100:
                    temp_output += "C"
                    value -= 100
                    continue
                elif value >= 50:
                    temp_output += "L"
                    value -= 50
                    continue
                elif value >= 10:
                    temp_output += "X"
                    value -= 10
                    continue
                elif value >= 5:
                    temp_output += "V"
                    value -= 5
                    continue
                elif value >= 1:
                    temp_output += "I"
                    value -= 1
                    continue
            output = temp_output + output
            decimal = decimal * 10
        return output
