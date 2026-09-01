class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        total = numbers[l] + numbers[r]
        while total != target and l < r:
            if total < target:
                l += 1
            if target < total:
                r -= 1
            total = numbers[l] + numbers[r]
        return [l+1,r+1]
        