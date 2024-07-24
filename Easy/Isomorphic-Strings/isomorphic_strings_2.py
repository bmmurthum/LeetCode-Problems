class Solution:
    def is_isomorphic_2(self, s: str, t: str) -> bool:

        map_s_t = {}
        map_t_s = {}

        if len(s) != len(t):
            return False

        for cs, ct in zip(s, t):
            if ct not in map_t_s and cs not in map_s_t:
                map_t_s[ct] = cs
                map_s_t[cs] = ct
            elif map_t_s.get(ct) != cs or map_s_t.get(cs) != ct:
                return False
        return True
