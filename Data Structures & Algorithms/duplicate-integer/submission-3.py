class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist = set()
        for i in nums:
            newlist.add(i)
        if len(newlist) == len(nums):
            return False
        return True

        