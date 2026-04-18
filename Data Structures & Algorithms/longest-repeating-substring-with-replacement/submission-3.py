class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        longest_len = 0
        char_count = {}
        max_freq = 0

        while i<=j and j < len(s):
            char_count[s[j]] = 1 + char_count.get(s[j], 0)
            max_freq = max(max_freq, char_count[s[j]])

            while (j-i+1) - max_freq > k:
                char_count[s[i]] -= 1
                i += 1

            longest_len = max(longest_len, j+1-i)
            j += 1 

        return longest_len