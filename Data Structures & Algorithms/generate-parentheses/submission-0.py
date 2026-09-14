class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        valid = ""
        def dfs(l, r, valid):
            if l > n or r > n:
                return

            if r > l:
                return

            if l == n and r == n:
                output.append(valid)
                return

            dfs(l+1, r, valid + "(")

            dfs(l, r+1, valid + ')')
        
        dfs(0, 0, valid)
        
        return output
            
            

        