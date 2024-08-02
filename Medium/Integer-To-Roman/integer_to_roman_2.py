class Solution:
    def int_to_roman_2(self, num: int) -> str:
        roman_values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        formatted = []
        for v, sym in roman_values:
            while num >= v:
                formatted.append(sym)
                num -= v
        return "".join(formatted)
