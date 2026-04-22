class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                area = h*(i-j)
                max_area = max(max_area, area)
                start = j
            stack.append((height, start))

        while stack:
            h, j = stack.pop()
            area = h*(n-j)
            max_area = max(max_area, area)

        return max_area