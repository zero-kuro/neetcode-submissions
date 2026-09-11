class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        output = intervals[0]
        end = output[1]
        removed = 0
        for interval in intervals[1:]:
            start = interval[0]
            if start >= end:
                end = interval[1]
            else:
                removed += 1
        return removed
        