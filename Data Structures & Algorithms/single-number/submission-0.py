class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = {}
        for i in nums:
            store[i] = store.get(i, 0) + 1
        for key, value in store.items():
            if value == 1:
                return key
        
        