class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                output.append(interval)
            elif interval[0] > newInterval[1]:
                output.append(newInterval)
                output.extend(intervals[i:])
                return output
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        output.append(newInterval)
        return output
            