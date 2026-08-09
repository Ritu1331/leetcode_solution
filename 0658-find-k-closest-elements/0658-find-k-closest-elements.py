import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = []
        ans = []

        for num in arr:
            dist = abs(num - x)
            heapq.heappush( heap, (-dist ,-num,num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            dist, neg_num, num = heapq.heappop(heap)
            ans.append(num)
        
        ans.sort()
        
        return ans 
        

        