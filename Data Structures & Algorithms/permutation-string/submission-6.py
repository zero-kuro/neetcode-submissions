class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = {}
        s2c = {}
        j = 0
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s1c[s1[i]] = s1c.get(s1[i],0) + 1
        for h in range(len(s1)):
            s2c[s2[h]] = s2c.get(s2[h],0) + 1
        while j + len(s1) <= len(s2):
            if s1c == s2c:
                return True
            s2c[s2[j]] -= 1
            if s2c[s2[j]] == 0:
                s2c.pop(s2[j])
            if j + len(s1) > len(s2) - 1:
                break
            s2c[s2[j+len(s1)]] = s2c.get(s2[j+len(s1)],0) + 1
            j += 1

        return False