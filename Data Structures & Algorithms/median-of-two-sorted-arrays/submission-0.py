class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            B, A = A, B
        total = len(A) + len(B)
        l = 0
        r = len(A)
        half = total // 2
        while l <= r:
            x = (l+r)//2
            y = half - x
            if x == 0:
                Aleft = float('-inf')
            else:
                Aleft = A[x-1]
            if x == len(A):
                Aright = float('inf')
            else:
                Aright = A[x]
            if y == 0:
                Bleft = float('-inf')
            else:
                Bleft = B[y-1]
            if y == len(B):
                Bright = float('inf')
            else:
                Bright = B[y]
            if Aleft <= Bright and Aright >= Bleft:
                if total % 2 == 1:
                    return float(min(Aright, Bright))
                else:
                    return float(((max(Aleft, Bleft)+min(Aright,Bright))/2))
            elif Aleft>Bright:
                r = x-1
            else:
                l = x+1





        
        