class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = nums[0]
        globalmax = nums[0]
        for n in nums[1:]:
        
            cursum = max(cursum + n,  n)

            globalmax = max(globalmax, cursum)
        return globalmax