class Solution(object):

    # Direction arrays (Up, Right, Down, Left)
    x = [-1, 0, 1, 0]
    y = [0, 1, 0, -1]

    def valid(self, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        return True

    def dfs(self, grid, n, m, i, j, vis):

        vis[i][j] = True

        for k in range(4):

            row = i + self.x[k]
            col = j + self.y[k]

            if (self.valid(row, col, n, m) and
                grid[row][col] == "1" and
                not vis[row][col]):

                self.dfs(grid, n, m, row, col, vis)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])

        vis = [[False] * m for _ in range(n)]

        count = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == "1" and not vis[i][j]:
                    count += 1
                    self.dfs(grid, n, m, i, j, vis)

        return count