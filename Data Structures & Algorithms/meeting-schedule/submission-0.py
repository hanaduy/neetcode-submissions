"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        result = []
        can_attend = True

        for interval in intervals:
            if not result :
                result.append(interval)
                prev_end = interval.end
            else:
                if interval.start < prev_end:
                    return False
                else:
                    result.append(interval)
                    prev_end = interval.end
        print(result)
        return True