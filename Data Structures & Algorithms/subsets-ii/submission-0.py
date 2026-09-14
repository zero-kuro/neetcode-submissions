class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = [[]]
        start = 0
        for i, num in enumerate(nums):
            
            if i > 0 and nums[i] == nums[i-1]:
                subset = output[start:]
            else:
                subset = output[:]

            dupe = []

            for sub in subset:
                dupe.append(sub + [num])
            
            start = len(output)
            output.extend(dupe)
        return output
        


        