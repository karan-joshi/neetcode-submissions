class Solution:
    def checkDuplicate(self, s: str, k:int) -> bool:
        unique_char = {}
        for c in s:
            unique_char[c] = unique_char.get(c, 0) + 1
        
        high_freq = 0
        for key, val in unique_char.items():
            high_freq = max(high_freq, val)
        
        return True if len(s) - high_freq <= k else False

    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        longest_len = 0

        while i<=j and j < len(s):
            if self.checkDuplicate(s[i:j+1], k):
                longest_len = max(longest_len, j+1-i)
                j += 1
            else:
                i += 1

        return longest_len