class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        i_list, j_list = set(), set()

        for i in range(len(matrix)): 
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    i_list.add(i)
                    j_list.add(j)

        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in i_list or j in j_list:
                    matrix[i][j] = 0
                