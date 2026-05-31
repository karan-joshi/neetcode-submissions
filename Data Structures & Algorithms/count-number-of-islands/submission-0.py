class Solution:
    def __init__(self):
        self.grid = None
        self.visited = None
    
    def dfs(self, i, j):
        if i < 0 or j < 0 or \
            i >= len(self.grid) or \
            j >= len(self.grid[0]) or \
            self.grid[i][j] == "0" or \
            self.visited[i][j] == 1:
            return

        self.visited[i][j] = 1
    
        self.dfs(i+1, j)
        self.dfs(i-1, j)
        self.dfs(i, j+1)
        self.dfs(i, j-1)
        
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[0]*len(grid[0]) for i in range(len(grid))]
        self.visited = visited
        self.grid = grid
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and self.visited[i][j] == 0:
                    islands += 1
                    self.dfs(i, j)

        return islands
