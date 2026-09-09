class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        i = 0
        furthest = 0
        count = 0
        while r < len(nums) - 1:
            for j in range(l,r+1):
                furthest = max(furthest, nums[j]+j)
            l = r + 1
            r = furthest
            count += 1
        return count
       
            