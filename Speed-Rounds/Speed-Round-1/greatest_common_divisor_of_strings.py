class Solution:
    """Problem provided by LeetCode"""

    def gcd_of_strings(self, str1: str, str2: str) -> str:
        """
        Finds the "greatest common denominator" between the two strings.

        Args:
            `str1`: First string.
            `str2`: Second string.
        Returns:
            `largest`: The largest common denominator.
        """

        # 30 min, 30 sec.
        # Burned time exploring a solution that wouldn't work.

        # Fixed after.
        # for i in range(1, (str_length // 2) + 1):
        #  - Necessary range change
        # for j in range(1, str_length // i):
        #  - Starting at 1 instead of 0 reduces redundance
        # if is_divisible and item > largest:
        #  - Didn't consider that sets may be enumerated in differing orders.
        # b = str2[pos : pos + length]
        #  - Overlooked `b` not being pulled from str2 instead of str1
        # elif str1 == str2:
        #     return str1
        #  - If they're equal, the answer is str1. No need to process.
        # temp_set.add(str1)
        #  - Always consider the full str1 to be something to look for as a
        #    GCD in str2.

        # Find repeats in str1
        temp_set = set()
        if len(str1) == 1:
            temp_set.add(str1)
        elif str1 == str2:
            return str1
        else:
            str_length = len(str1)
            for i in range(1, (str_length // 2) + 1):
                if str_length % i != 0:
                    continue
                a = str1[:i]
                is_divisible = True
                for j in range(1, str_length // i):
                    pos = j * i
                    b = str1[pos : pos + i]
                    if a != b:
                        is_divisible = False
                        break
                if is_divisible:
                    temp_set.add(a)
            temp_set.add(str1)

        # If found nothing good in str1
        if len(temp_set) == 0:
            return ""

        # Look for the largest item in the last set that is divisible in the second string.
        largest = ""
        for item in temp_set:
            length = len(item)
            str_length = len(str2)
            if str_length % length != 0:
                continue
            is_divisible = True
            for j in range(str_length // length):
                pos = j * length
                b = str2[pos : pos + length]
                if item != b:
                    is_divisible = False
                    break
            if is_divisible and item > largest:
                largest = item
        return largest
