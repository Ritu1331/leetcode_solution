
import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        projects = []

        for i in range(len(profits)):
            projects.append((capital[i], profits[i]))

        projects.sort()

        max_heap = []
        i = 0

        for _ in range(k):

            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w