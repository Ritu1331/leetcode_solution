class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        import heapq
        adj = [[] for _ in range(n + 1)]

        for u , v , w in times:
            adj[u].append((v,w)) #node , weight
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = []
        heapq.heappush(pq,(0,k)) #(dist : w , src: k)

        while pq:
            d , node  = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for neigh , w in adj[node]:
                if d + w < dist[neigh]:
                    dist[neigh] = d + w
                    heapq.heappush(pq ,(dist[neigh] , neigh))
        
        ans = 0

        for i in range(1, n + 1):

            if dist[i] == float('inf'):
                return -1

            ans = max(ans, dist[i])

        return ans




        