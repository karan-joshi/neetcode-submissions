class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        longest_length = 0
        for n in hash_set:
            if n-1 in hash_set:
                continue
            
            n_next = n+1
            seq_len = 1
            while n_next in hash_set:
                n_next += 1
                seq_len += 1
            
            longest_length = max(longest_length, seq_len)

        return longest_length