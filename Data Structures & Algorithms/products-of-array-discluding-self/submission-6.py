class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        rightprod = 1
        for i, left in enumerate(nums):
            if i == 0:
                output[i] = 1
            else:
                output[i] = output[i-1] * nums[i-1]
        for j, right in enumerate(nums[::-1]):
            output[len(nums) - 1 - j] *= rightprod
            rightprod *= right



        return output