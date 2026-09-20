class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        f = nums[:-1]
        s = nums[1:]

        def solve(l):
            memo = {}

            def dfs(i):

                if i >= len(f):
                    return 0
                
                if i in memo:
                    return memo[i]
                
                else:
                    total = max(l[i] + dfs(i+2), dfs(i+1))
                    memo[i] = total
                    return memo[i]
            return dfs(0)
        return max(solve(f), solve(s))