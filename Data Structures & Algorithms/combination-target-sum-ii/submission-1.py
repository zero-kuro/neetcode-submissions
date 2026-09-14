class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        poss = []
        output = []
        remaining = target
        i = 0
        def dfs(i, remaining, poss):
            if remaining == 0:
                output.append(poss)
                return
            
            if remaining < 0 or i >= len(candidates):
                return

            ni = i+1
            while ni < len(candidates) and candidates[ni] == candidates[i]:
                ni += 1

            dfs(ni, remaining, poss)

            dfs(i+1, remaining-candidates[i], poss + [candidates[i]])

        dfs(0, remaining, poss)
        return output