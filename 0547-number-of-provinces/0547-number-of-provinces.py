class Solution(object):
    def findCircleNum(self, isConnected):

        n = len(isConnected)

        visited = [False] * n

        count = 0

        def dfs(i):
            visited[i] = True

            for j in range(n):

                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        for i in range(n):

            if not visited[i]:
                count += 1
                dfs(i)

        return count