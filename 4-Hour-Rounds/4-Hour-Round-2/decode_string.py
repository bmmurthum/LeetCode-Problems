"""Problem from LeetCode.com"""

# Ignore the advice to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def decode_string(self, s: str) -> str:
        """
        Returns a decoded string.

        "2[abc]3[cd]ef" -> "abcabccdcdcdef"

        Args:
            `s`: The encoded string.
        Returns:
            `output`: The fully decoded string.
        """

        # Ex: [['2','s'],['3','ab']]
        our_stack = []
        output = ""

        # Build a stack that keeps a record of how many of this element and the
        # ones after will be repeated.
        i = 0
        while i < len(s):
            # At number
            # - Add to the stack
            if s[i].isnumeric():
                # Build multiple digit numbers
                quantity = s[i]
                count = 1
                for j in range(i + 1, len(s)):
                    if s[j].isnumeric():
                        quantity += s[j]
                        count += 1
                    else:
                        break
                our_stack.append([quantity, ""])
                i += count + 1
                continue
            # At letter
            # - If stack exists, add to last element's data
            # - Else, append to the final output
            if s[i].isalpha():
                if len(our_stack) > 0:
                    if our_stack[-1][1] == "":
                        our_stack[-1][1] = s[i]
                    else:
                        our_stack[-1][1] += s[i]
                else:
                    output += s[i]
                i += 1
                continue
            # At end-bracket
            # - If stack is multiple, transform stack
            # - Else, append to the final output
            if s[i] == "]":
                if len(our_stack) == 1:
                    for _ in range(int(our_stack[0][0])):
                        output += our_stack[0][1]
                    our_stack.pop()
                else:
                    temp = ""
                    for _ in range(int(our_stack[-1][0])):
                        temp += our_stack[-1][1]
                    our_stack[-2][1] += temp
                    our_stack.pop()
                i += 1
                continue

        # Return the built string
        return output
