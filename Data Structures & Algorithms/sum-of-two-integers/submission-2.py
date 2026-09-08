class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1

        a = a & mask
        b = b & mask

        while b != 0:
            carry = ((a&b)<<1) & mask
            a = (a ^ b) & mask
            b = carry

        if a & (1 << 31):
            return -((a ^ mask) + 1)
        
        return a


            

            
        