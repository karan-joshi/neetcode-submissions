class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [nums[0]]
        suffix_prod = [nums[-1]]

        for i in range(1, len(nums)):
            prefix_prod.append(nums[i]*prefix_prod[i-1])

        for i in range(len(nums)-2, -1, -1):
            suffix_prod.append(nums[i]*suffix_prod[-1])

        ans = []

        for i in range(len(nums)):
            if i == 0:
                ans.append(suffix_prod[len(nums)-2])
            elif i == len(nums)-1:
                ans.append(prefix_prod[i-1])
            else:
                ans.append(prefix_prod[i-1]*suffix_prod[len(nums)-2-i])

        return ans