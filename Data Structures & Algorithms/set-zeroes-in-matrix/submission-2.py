class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix[0]), len(matrix)
        rows = set()
        cols = set()
        
        for i in range(n): #rows
            for j in range(m): #cols
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            matrix[row][:] = [0] * m
        for col in cols:
            for r in range(n):
                matrix[r][col] = 0
            
        

        
        