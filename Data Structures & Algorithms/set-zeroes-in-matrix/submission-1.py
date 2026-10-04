class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix[0]), len(matrix)
        rec = []
        
        
        for i in range(m):
            for j in range(n):
                if matrix[j][i] == 0:
                    rec.append((j,i))
        for row, col in rec:
            matrix[row][:] = [0] * m
            for h in range(n):
                matrix[h][col] = 0
            
        

        
        