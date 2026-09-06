"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        if intervals == []:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        endtime = []

        for meeting in intervals:
            if endtime and meeting.start >= endtime[0]:
                heapq.heappop(endtime)
            heapq.heappush(endtime, meeting.end)
        return len(endtime)

