class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        if len(intervals) == 1:
            return [interval for interval in intervals]
        
        curr = intervals[0]

        for i in range(1, len(intervals)):
            nextint = intervals[i]

            if nextint[0] <= curr[1]:
                curr[0] = min(curr[0], nextint[0])
                curr[1] = max(curr[1], nextint[1])
            else:
                merged.append(curr)
                curr = nextint
        merged.append(curr)

        return merged
            