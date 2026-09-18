class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones:
            stones.sort()
            if len(stones) == 1:
                return stones[0]    
            highest = stones.pop()
            second = stones.pop()
            stones.append(highest-second)
        return 0
            
            

        