class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort()

        merged = []
        start, end = intervals[0]

        
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start <= end:  
                end = max(end, curr_end)
            else:
                merged.append([start, end])
                start, end = curr_start, curr_end

       
        merged.append([start, end])

        return merged