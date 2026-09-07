class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] #output of 0 is 0
        offset = 1 #start with offset 1 
        for i in range(1, n+1): #from second number(1) to n
            if i == offset*2: #when reach power of 2, offset increases to i
                offset = i

            bit = 1 + output[i - offset] #1 + since the first bit is 1, then look at the prev output

            output.append(bit)
        return output

