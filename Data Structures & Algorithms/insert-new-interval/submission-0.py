class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new_start, new_end = newInterval[0], newInterval[1]
        i,n = 0,len(intervals)
        left, right = new_start, new_end

        while i<n and new_start > intervals[i][1]:
            result.append(intervals[i])
            i+=1

        while i<n and new_end >= intervals[i][0]:
            left = min(left, intervals[i][0])
            right = max(right, intervals[i][1])
            i+=1
        result.append([left,right])

        while i<n and new_end < intervals[i][0]:
            result.append(intervals[i])
            i+=1
        
        return result
