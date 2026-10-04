class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(x, y, px, py):

            visited[x][y] = True

            for dx, dy in directions:

                nx = x + dx
                ny = y + dy

                # Outside grid
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                # Different character
                if grid[nx][ny] != grid[x][y]:
                    continue

                # Parent cell → ignore
                if nx == px and ny == py:
                    continue

                # Already visited same-character cell
                if visited[nx][ny]:
                    return True

                # Continue DFS
                if dfs(nx, ny, x, y):
                    return True

            return False

        for i in range(m):
            for j in range(n):

                if not visited[i][j]:

                    if dfs(i, j, -1, -1):
                        return True

        return False


        """Time  = O(m × n)
Space = O(m × n)   # DFS recursion stack"""
        