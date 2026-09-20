class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits)-1,-1,-1):
            if i != 0 and digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
            elif i == 0 and digits[i] == 10:
                digits[i] = 0
                digits.insert(0,1)
            else:

                break
        return digits