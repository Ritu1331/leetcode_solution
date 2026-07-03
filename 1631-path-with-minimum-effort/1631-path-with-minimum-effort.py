import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        m = len(heights)
        n = len(heights[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]

        pq = []
        heapq.heappush(pq, (0, (0, 0)))

        while pq:
            effort, (row, col) = heapq.heappop(pq)

            if effort > dist[row][col]:
                continue

            for k in range(4):
                r = row + x[k]
                c = col + y[k]

                if r < 0 or c < 0 or r >= m or c >= n:
                    continue

                abs_diff = abs(heights[row][col] - heights[r][c])

                new_effort = max(effort, abs_diff)

                if new_effort < dist[r][c]:
                    dist[r][c] = new_effort
                    heapq.heappush(pq, (new_effort, (r, c)))

        return dist[m - 1][n - 1]