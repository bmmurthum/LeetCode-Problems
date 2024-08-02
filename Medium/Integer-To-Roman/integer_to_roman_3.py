class Solution:
    def int_to_roman_3(self, num: int) -> str:
        s = [int(c) for c in str(num)]
        n = len(s)

        if s[-1] <= 3:
            rom = "I" * s[-1]
        elif s[-1] == 4:
            rom = "IV"
        elif s[-1] < 9:
            rom = "V" + (s[-1] - 5) * "I"
        elif s[-1] == 9:
            rom = "IX"

        if len(s) > 1:
            if s[-2] <= 3:
                rom = "X" * s[-2] + rom
            elif s[-2] == 4:
                rom = "XL" + rom
            elif s[-2] < 9:
                rom = "L" + (s[-2] - 5) * "X" + rom
            elif s[-2] == 9:
                rom = "XC" + rom

        if len(s) > 2:
            if s[-3] <= 3:
                rom = "C" * s[-3] + rom
            elif s[-3] == 4:
                rom = "CD" + rom
            elif s[-3] < 9:
                rom = "D" + (s[-3] - 5) * "C" + rom
            elif s[-3] == 9:
                rom = "CM" + rom
        if len(s) > 3:
            rom = s[0] * "M" + rom
        return rom
