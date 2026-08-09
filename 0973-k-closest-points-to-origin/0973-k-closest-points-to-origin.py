import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        ans = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))

        while k:
            dist, x, y = heapq.heappop(heap)
            ans.append([x, y])
            k -= 1

        return ans

        