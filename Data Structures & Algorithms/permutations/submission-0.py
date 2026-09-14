class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        poss = []
        output = []
        def dfs(poss):
            if len(poss) == len(nums):
                output.append(poss)
                return
            for num in nums:
                if num not in poss:
                    dfs(poss + [num])
        dfs(poss)
        return output

                        



        