class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = [0]*len(height)

        for i in range(len(height)):
            if i>0:
                max_left.append(max(max_left[i-1], height[i-1]))
            else:
                max_left.append(0)
        
        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])

        water_stored = 0

        for i in range(len(height)):
            if min(max_left[i], max_right[i]) > height[i]:
                water_stored += min(max_left[i], max_right[i]) - height[i]

        return water_stored
    
