class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count_s1 = {}

        for c in s1:
            count_s1[c] = 1 + count_s1.get(c,0)

        need = len(count_s1)
        for i in range(len(s2)):
            count_s2 = {}
            curr = 0
            for j in range(i, len(s2)):        
                count_s2[s2[j]] = 1 + count_s2.get(s2[j], 0)
                if count_s1.get(s2[j], 0) < count_s2[s2[j]]:
                    break
                if count_s1.get(s2[j], 0) == count_s2[s2[j]]:
                    curr += 1
                if curr == need:
                    return True
                
        return False

            



