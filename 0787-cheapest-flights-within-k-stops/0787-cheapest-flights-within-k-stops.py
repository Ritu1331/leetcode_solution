class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        res = [float('inf')] * n
        res[src] = 0

        for i in range(k + 1):

            temp = res[:]

            for s, d, wt in flights:

                if res[s] != float('inf') and temp[d] > res[s] + wt:

                    temp[d] = res[s] + wt

            res = temp

        if res[dst] == float('inf'):
            return -1

        return res[dst]