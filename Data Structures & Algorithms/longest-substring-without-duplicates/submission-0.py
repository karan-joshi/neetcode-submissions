class Solution:
    def checkDuplicate(self, s: str) -> bool:
        return True if len(set(s)) == len(s) else False
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        longest_len = 0

        while i <= j and j < len(s):
            if self.checkDuplicate(s[i:j+1]):
                longest_len = max(longest_len, (j+1-i))
                j += 1
            else:
                i += 1

        return longest_len