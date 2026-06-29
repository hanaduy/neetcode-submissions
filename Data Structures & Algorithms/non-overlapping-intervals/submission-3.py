class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = []
        count = 0
        
        for interval in intervals:
            if not result:
                result.append(interval)
                prev_end = interval[1]
            else:
                cur_start, cur_end = interval[0], interval[1]
                if cur_start < prev_end:
                    count +=1
                    prev_end = min(prev_end, cur_end)
                    result[-1][1] = min(prev_end, cur_end)
                else:
                    prev_end = cur_end
                    result.append(interval)
        print(result)
        return count
