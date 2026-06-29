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
        
        heap = []
        intervals.sort(key=lambda x: x.start)
        heapq.heappush(heap, intervals[0].end)

        for interval in intervals[1:]:
            print(heap)
            end_time = heapq.heappop(heap)
            if interval.start < end_time:
                heapq.heappush(heap,end_time)
                heapq.heappush(heap,interval.end)
            else:
                heapq.heappush(heap,interval.end)
        return len(heap)


        