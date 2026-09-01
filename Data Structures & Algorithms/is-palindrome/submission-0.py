class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for h in s:
            if h.isalnum():
                s1 += h
        s1 = s1.replace(' ', "").lower()
        m = len(s1) // 2
        front = ""
        back = ""
        if len(s1) % 2 == 0:
            for i in range(m):
                front += s1[i]
            for j in range(m,len(s1)):
                back += s1[j]
        else:
            for i in range(m):
                front += s1[i]
            for j in range(m+1,len(s1)):
                back += s1[j]
        if front == back[::-1]:
            return True
        else:
            return False
            
            