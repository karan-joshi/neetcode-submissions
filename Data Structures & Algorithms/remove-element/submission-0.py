class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        indices = []

        for i in range(0, len(nums)):
            if nums[i] == val:
                indices.append(i)

        count = 0
        while indices:
            index = indices.pop()
            nums[index] = nums[len(nums)-1-count]
            count += 1

        return len(nums) - count
            