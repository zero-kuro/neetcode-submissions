class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying = prices[0]
        maxpro = 0
        for i in range(len(prices)):
            currpro = max(prices[i]-buying, 0)
            if maxpro < currpro:
                maxpro = currpro
            buying = min(buying, prices[i])
        return maxpro
        