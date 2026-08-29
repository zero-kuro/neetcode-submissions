class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterdic = {}
        counter = 1
        for num in nums:
            if num not in counterdic:
                counterdic[num] = 1
            elif num in counterdic:
                counterdic[num] += 1
        quota = 0
        output = []
        sorteddic = dict(sorted(counterdic.items(), key=lambda item: item[1], reverse=True))
        while quota < k:
            output.append(list(sorteddic.keys())[quota])
            quota += 1
        return output

            
            