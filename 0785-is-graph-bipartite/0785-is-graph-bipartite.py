class Solution(object):

    def dfs(self, node, color, colors, graph):

        colors[node] = color

        for neigh in graph[node]:

            if colors[neigh] == -1:

                colors[neigh] = 1 - color

                self.dfs(neigh, 1 - color, colors, graph)

            elif colors[neigh] == color:

                self.res = False

    def isBipartite(self, graph):

        n = len(graph)

        colors = [-1] * n

        self.res = True

        for i in range(n):

            if colors[i] == -1:

                self.dfs(i, 0, colors, graph)

        return self.res