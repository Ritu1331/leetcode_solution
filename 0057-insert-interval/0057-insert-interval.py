class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        
        # If empty
        if not intervals:
            return [newInterval]

        # Step 1: Add new interval
        intervals.append(newInterval)

        # Step 2: Sort
        intervals.sort()

        # Step 3: Merge (same as your previous code)
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