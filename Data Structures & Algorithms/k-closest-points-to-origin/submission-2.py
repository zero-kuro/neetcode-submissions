class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        distpoint = []
        for point in points:
            distance = [point[0]**2 + point[1]**2]
            distpoint.append([distance,point])
        heapq.heapify_max(distpoint)
        count = 0
        while k < len(distpoint):
            heapq.heappop_max(distpoint)
        cor = []
        for co in list(distpoint):
            cor.append((co[1]))
        return cor
        