class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        numsset = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in numsset:
                continue
            else:
                current = num
                count = 1
                while current + 1 in numsset:
                    current += 1
                    count += 1
                if count > longest:
                    longest = count
        return longest
                
