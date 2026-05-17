class CountSquares:

    def __init__(self):
        self.points_count = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.points_count[point[0]][point[1]] += 1
            

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point

        for y2 in self.points_count[x1]:
            side = y2-y1
            if side == 0:
                continue
            
            x3, x4 = x1 + side, x1 - side
            res += (self.points_count[x1][y2]*self.points_count[x3][y1]*self.points_count[x3][y2])
            res += (self.points_count[x1][y2]*self.points_count[x4][y1]*self.points_count[x4][y2])
            
        return res
