class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix)-1
        row_end = len(matrix[0])-1

        while l < r:
            mid = (l+r)//2
            print(mid, l, r)
            if matrix[mid][row_end] == target:
                return True
            elif matrix[mid][row_end] < target:
                l = mid+1
            else:
                r = mid

        row_index = r
        l = 0
        r = len(matrix[0])-1

        while l <= r:
            mid = (l+r)//2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] < target:
                l = mid+1
            else:
                r = mid-1

        return False
