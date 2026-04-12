class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = dict()

        for i in range(len(nums)):
            if target - nums[i] in n_map:
                return [n_map[target - nums[i]], i]
            
            n_map[nums[i]] = i


        