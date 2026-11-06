class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        # Sort logs according to time
        logs.sort(key=lambda a: a[1])

        # Sort queries but preserve original indices
        q = sorted((time, i) for i, time in enumerate(queries))

        ans = [0] * len(queries)

        freq = {}
        left = 0
        right = 0
        active = 0

        for time, idx in q:

            # Add logs that occurred up to query time
            while right < len(logs) and logs[right][1] <= time:

                server = logs[right][0]

                if freq.get(server, 0) == 0:
                    active += 1

                freq[server] = freq.get(server, 0) + 1

                right += 1

            # Remove logs outside the time window
            while left < right and logs[left][1] < time - x:

                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                left += 1

            # Store answer at original query index
            ans[idx] = n - active

        return ans


        