import heapq
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        heap = []
        ans = []

        for i in range(len(mat)):
            soldier = sum(mat[i])

            heapq.heappush(heap , ( - soldier , -i , i))

            if len(heap) > k:
                heapq.heappop(heap)
    
        while heap:
            
            soldier, index, i = heapq.heappop(heap)
            ans.append(i)

        ans.reverse()

        return ans




        