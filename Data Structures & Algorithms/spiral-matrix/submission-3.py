class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        res = []
    
        while l <= r and t <= b:
            start, end = l, r
            
            while start <= end:
                res.append(matrix[t][start])
                start += 1
            start = l
            t += 1
            
            for j in range(t,b+1):
                res.append(matrix[j][r])
            r -= 1

            if t > b or r < l:
                break
            
            while end-1 >= start:
                res.append(matrix[b][end-1])
                end -= 1
            end = r
            b -= 1

            for h in range(b,t-1, -1):
                res.append(matrix[h][l])
            l += 1
            
        return(res)

            
            