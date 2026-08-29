class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorteds, sortedt = "".join(sorted(s)), "".join(sorted(t))
        if sorteds == sortedt:
            return True
        else:
            return False
        