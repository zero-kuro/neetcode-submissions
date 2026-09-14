class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        remaining = target
        index = 0
        combo = []
        def dfs(index, remaining, combo):
            if remaining == 0:
                output.append(combo)
                return
            if remaining < 0 or index >= len(nums):
                return
            
            dfs(index, remaining - nums[index], combo + [nums[index]])

            dfs(index+1, remaining, combo)
        dfs(0, target, combo)

        return output
        