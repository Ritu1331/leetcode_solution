import heapq

class Solution(object):
    def scheduleCourse(self, courses):

        courses.sort(key=lambda x: x[1])

        max_heap = []
        time = 0

        for duration, lastDay in courses:

            time += duration
            heapq.heappush(max_heap, -duration)

            if time > lastDay:
                longest = -heapq.heappop(max_heap)
                time -= longest

        return len(max_heap)