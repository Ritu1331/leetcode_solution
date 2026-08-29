class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
    
        while len(stones) > 1:
            stones.sort()

            y = stones.pop()   # heaviest
            x = stones.pop()   # second heaviest

            if y != x:
                stones.append(y - x)

        if stones:
            return stones[0]
        return 0
        