class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        for c in t:
            if c not in s_map or s_map.get(c) == 0:
                return False
            
            s_map[c] = s_map.get(c,0) - 1

        for key, val in s_map.items():
            if val > 0:
                return False

        return True