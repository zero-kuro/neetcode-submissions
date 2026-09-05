class Solution:
    def minWindow(self, s: str, t: str) -> str:
        bestlength = float("inf")

        if len(s) < len(t): 
            return ""
        l = 0

        need = {}
        for letter in t:
            need[letter] = need.get(letter, 0) + 1
        
        window = {}

        for r in range(len(s)):
            if s[r] in need:
                window[s[r]] = window.get(s[r], 0) + 1
            
            valid = True
            for letter in need:
                if window.get(letter, 0) < need[letter]:
                    valid = False
                    break
    
            while valid:
                
                length = r - l + 1
                if length < bestlength:
                    bestlength = length
                    bestl = l
                    bestr = r
                
                if s[l] in need:
                    window[s[l]] -= 1
                l += 1

                for letter in need:
                    if window.get(letter, 0) < need[letter]:
                        valid = False
                        break
        if bestlength == float('inf'):
            return ""




        return s[bestl:bestr + 1]
        