class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq

        n = len(grid)
        x = [1 , -1 , 0 , 0]
        y = [0 , 0, 1 ,-1]

        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        pq = []

        heapq.heappush(pq,( dist[0][0] , 0 ,0)) #water_level , row , col

        while pq:
            d , r ,c  = heapq.heappop(pq)

            if d > dist[r][c]:
                continue
            
            if r == n-1 and c == n-1:
                return d

            
            for i in range(4):
                row = r + x[i]
                col = c + y[i]

                if 0 <= row < n and 0 <= col < n:
                    new_dist = max( d , grid[row][col])

                    if new_dist < dist[row][col]:
                        dist[row][col] = new_dist
                        heapq.heappush(pq , (dist[row][col] , row , col))
                

          
'''Time Complexity: O(n² log n)
Space Complexity: O(n²)'''