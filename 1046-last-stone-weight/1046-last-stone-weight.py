class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
    
        """while len(stones) > 1:
            stones.sort()

            y = stones.pop()   # heaviest
            x = stones.pop()   # second heaviest

            if y != x:
                stones.append(y - x)

        if stones:
            return stones[0]
        return 0"""


        import heapq
        stones = [-stone for stone in stones]

        # Convert list into heap
        heapq.heapify(stones)

        while len(stones) > 1:

            # Get heaviest stone
            stone1 = -heapq.heappop(stones)

            # Get second heaviest stone
            stone2 = -heapq.heappop(stones)

            # If weights are different
            if stone1 != stone2:

                # Difference is the remaining stone
                new_stone = stone1 - stone2

                # Add it back to heap
                heapq.heappush(stones, -new_stone)

        # If one stone remains, return it
        if stones:
            return -stones[0]

        return 0
        