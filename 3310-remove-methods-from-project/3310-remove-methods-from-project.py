class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """

        # Step 1: Build the graph
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        # Step 2: Find all suspicious methods using DFS
        suspicious = set()

        def dfs(node):
            if node in suspicious:
                return

            suspicious.add(node)

            for nei in graph[node]:
                dfs(nei)

        dfs(k)

        # Step 3: Check if any non-suspicious method
        # calls a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Step 4: Return all non-suspicious methods
        ans = []

        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans

        '''sc and tc = (n + m)'''