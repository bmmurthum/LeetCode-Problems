class Solution:
    def is_isomorphic_3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_unique = set(s)

        for s_char in s_unique:
            start = 0
            s_index = s.find(s_char, start)
            t_char = t[s_index]
            while s_index != -1:
                start = s_index + 1
                s_index = s.find(s_char, start)
                t_index = t.find(t_char, start)
                if s_index != t_index:
                    return False

        return True
