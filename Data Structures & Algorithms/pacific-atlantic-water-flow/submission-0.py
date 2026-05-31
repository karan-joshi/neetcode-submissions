class Solution:
    def __init__(self):
        self.oceans = {'atlantic': set(), 'pacific': set()}
        self.heights = None

    def dfs(self, i, j, ocean, prev):
        if i<0 \
            or j<0 \
            or i>=len(self.heights) \
            or j>=len(self.heights[0]) \
            or self.heights[i][j] < prev \
            or (i,j) in self.oceans[ocean]:
            return

        self.oceans[ocean].add((i,j))

        self.dfs(i+1, j, ocean, self.heights[i][j])
        self.dfs(i-1, j, ocean, self.heights[i][j])
        self.dfs(i, j+1, ocean, self.heights[i][j])
        self.dfs(i, j-1, ocean, self.heights[i][j])
        
        return
        

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        pacific_set = set()
        atlantic_set = set()

        for j in range(len(heights[0])):
            pacific_set.add((0,j))

        for i in range(1, len(heights)):
            pacific_set.add((i,0))

        for j in range(len(heights[0])):
            atlantic_set.add((len(heights)-1, j))
        
        for i in range(0, len(heights)-1):
            atlantic_set.add((i, len(heights[0])-1))

        for (i,j) in atlantic_set:
            self.dfs(i, j, 'atlantic', 0)
        
        for (i,j) in pacific_set:
            self.dfs(i, j, 'pacific', 0)
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in self.oceans['pacific'] and (i,j) in self.oceans['atlantic']:
                    res.append([i,j])

        return res

        