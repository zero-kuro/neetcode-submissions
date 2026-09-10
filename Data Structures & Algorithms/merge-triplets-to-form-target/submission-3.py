class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #if one of the triplets in target, should keep track right
        newlist = []
        for i in range(len(triplets)):
            if all(triplets[i][j] <= target[j] for j in range(len(triplets[i]))):
                    newlist.append(triplets[i])
                    
        for k in range(len(target)):
            if not any(target[k] == newl[k] for newl in newlist):
                return False
        return True
            
                

        