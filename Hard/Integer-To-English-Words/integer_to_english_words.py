"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def number_to_words(self, num: int) -> str:
        """
        Converts an integer to english word representation.

        Range 0 -> 2,147,483,648

        Args:
            `num`: The given integer to convert.
        Returns:
            `output`: The return string.
        """

        # To generate the string as we process.
        output = ""

        # Quick numbers to have.
        unique_numbers = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        # Handle edge-case.
        if num == 0:
            return "Zero"

        # Pad with zeroes for string truncation.
        num_with_preceding_zeroes = str(num)
        for _ in range(10 - len(str(num))):
            num_with_preceding_zeroes = "0" + num_with_preceding_zeroes

        # Build a english string starting with largest decimals places.
        billion_chunk = int(num_with_preceding_zeroes[0])
        if billion_chunk > 0:
            output = unique_numbers[billion_chunk] + " Billion"
        million_chunk = int(num_with_preceding_zeroes[1:4])
        if million_chunk > 0:
            if million_chunk in unique_numbers:
                # "Twenty Million"
                output += " " + unique_numbers[million_chunk] + " Million"
            else:
                # 413 -> 13 : "Four Hundred"
                if million_chunk > 99:
                    temp = million_chunk // 100
                    output += " " + unique_numbers[temp] + " Hundred"
                    million_chunk -= temp * 100
                # 23 -> 3 : "Twenty"
                if million_chunk > 19:
                    temp = (million_chunk // 10) * 10
                    output += " " + unique_numbers[temp]
                    million_chunk -= temp
                    if million_chunk in unique_numbers:
                        output += " " + unique_numbers[million_chunk]
                # 8 -> _ : "Eight"
                else:
                    if million_chunk in unique_numbers:
                        output += " " + unique_numbers[million_chunk]
                # "Million"
                output += " Million"
        thousands_chunk = int(num_with_preceding_zeroes[4:7])
        if thousands_chunk > 0:
            if thousands_chunk in unique_numbers:
                output += " " + unique_numbers[thousands_chunk] + " Thousand"
            else:
                if thousands_chunk > 99:
                    temp = thousands_chunk // 100
                    output += " " + unique_numbers[temp] + " Hundred"
                    thousands_chunk -= temp * 100
                if thousands_chunk > 19:
                    temp = (thousands_chunk // 10) * 10
                    output += " " + unique_numbers[temp]
                    thousands_chunk -= temp
                    if thousands_chunk in unique_numbers:
                        output += " " + unique_numbers[thousands_chunk]
                else:
                    if thousands_chunk in unique_numbers:
                        output += " " + unique_numbers[thousands_chunk]
                output += " Thousand"
        ones_chunk = int(num_with_preceding_zeroes[7:10])
        if ones_chunk > 0:
            if ones_chunk > 99:
                temp = ones_chunk // 100
                output += " " + unique_numbers[temp] + " Hundred"
                ones_chunk -= temp * 100
            if ones_chunk > 19:
                temp = (ones_chunk // 10) * 10
                output += " " + unique_numbers[temp]
                ones_chunk -= temp
                if ones_chunk in unique_numbers:
                    output += " " + unique_numbers[ones_chunk]
            elif ones_chunk == 0:
                pass
            else:
                if ones_chunk in unique_numbers:
                    output += " " + unique_numbers[ones_chunk]

        # Return the full string
        output = output.strip()
        return output
