class Solution:
    def checkValidString(self, s: str) -> bool:
        opens = []
        stars = []

        for i, char in enumerate(s):
            if char == '(':
                opens.append(i)
        
            elif char == '*':
                stars.append(i)
        
            else:
                if opens:
                    opens.pop()
                
                elif stars:
                    stars.pop()
                
                else:
                    return False
        if len(opens) > len(stars):
            return False
        while opens:
            lastopen = opens[-1]
            laststar = stars[-1]

            if lastopen < laststar:
                opens.pop()
                stars.pop()
            else:
                return False
        return True
            
            