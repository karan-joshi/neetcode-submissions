class Solution:
    def __init__(self):
        self.visiting = set()
        self.pre_map = {}

    def dfs(self, crs):
        if crs in self.visiting:
            return False
        if self.pre_map[crs] == []:
            return True

        self.visiting.add(crs)
        for pre in self.pre_map[crs]:
            if not self.dfs(pre):
                return False
        self.visiting.remove(crs)
        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        self.pre_map = {i: [] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            self.pre_map[course].append(pre_req)

        for i in range(numCourses):
            if not self.dfs(i):
                return False

        return True

