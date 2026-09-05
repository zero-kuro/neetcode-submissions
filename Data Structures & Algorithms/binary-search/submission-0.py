class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            n = (l+r) // 2
            if target == nums[n]:
                return n
            elif target > nums[n]:
                l = n + 1
            else:
                r = n - 1
        return -1

        