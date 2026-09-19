class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        r = max(piles)
        l = 1
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i/k)
            if hours > h:
                l = k + 1
            else:
                res = min(k, res)
                r = k - 1
        return res
        