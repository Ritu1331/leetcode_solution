class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import heapq

        # Count frequency
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        # Max heap
        heap = []

        for count in freq.values():
            heapq.heappush(heap, -count)

        time = 0

        while heap:

            temp = []

            # One cycle = n + 1
            for i in range(n + 1):

                if heap:
                    count = -heapq.heappop(heap)
                    count -= 1

                    if count > 0:
                        temp.append(count)

                    time += 1

                elif temp:
                    time += 1

                else: #when heap and temp both empty
                    break

            # Put remaining tasks back
            for count in temp:
                heapq.heappush(heap, -count)

        return time
        