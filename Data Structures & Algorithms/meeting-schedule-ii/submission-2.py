"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        heap = []
        heapq.heappush(heap,intervals[0].end)

        for interval in intervals[1:]:
            prev_end = heapq.heappop(heap)

            if interval.start < prev_end:
                heapq.heappush(heap,prev_end)
                heapq.heappush(heap,interval.end)
            else:
                heapq.heappush(heap,interval.end)
                
        return len(heap)
        