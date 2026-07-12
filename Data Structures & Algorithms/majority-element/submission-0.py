
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}

        for n in nums:
            if n not in count_map:
                count_map[n] = 0
            
            count_map[n] += 1

        for key, value in count_map.items():
            if value > len(nums)/2:
                return key