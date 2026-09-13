class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        output.append([])
        for num in nums:
            dupe = []
            for i in output:
                dupe.append(i + [num])
            output.extend(dupe)
        return output

            
        