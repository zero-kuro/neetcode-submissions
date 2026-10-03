class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        res = []
    
        while l <= r and t <= b:
            
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t += 1
            
            for j in range(t,b+1):
                res.append(matrix[j][r])
            r -= 1

            if t > b or r < l:
                break
            
            for k in range(r,l-1, -1):
                res.append(matrix[b][k])
            b -= 1

            for h in range(b,t-1, -1):
                res.append(matrix[h][l])
            l += 1
            
        return(res)
