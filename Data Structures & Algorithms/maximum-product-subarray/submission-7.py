class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]
        if len(nums) == 1:
            return nums[0]
        for n in nums[1:]:
            old_max = curr_max
            old_min = curr_min

            curr_max = max(n, old_max * n, old_min * n)
            curr_min = min(n, old_max * n, old_min * n)

            global_max = max(global_max, curr_max)
            
            
        return global_max
