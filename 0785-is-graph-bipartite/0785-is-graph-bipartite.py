class Solution(object):

    def dfs(self, node, color, colors, graph):

        # Color the current node
        colors[node] = color

        # Visit all neighbours
        for neigh in graph[node]:

            # If neighbour is not colored
            if colors[neigh] == -1:

                # Color it with opposite color
                if not self.dfs(neigh, 1 - color, colors, graph):
                    return False

            # If neighbour has same color
            elif colors[neigh] == color:
                return False

        return True


    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        n = len(graph)

        # -1 = Not Colored
        colors = [-1] * n

        # Graph may be disconnected
        for i in range(n):

            if colors[i] == -1:

                if not self.dfs(i, 0, colors, graph):
                    return False

        return True