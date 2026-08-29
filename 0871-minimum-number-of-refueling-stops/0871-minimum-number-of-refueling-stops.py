class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        import heapq
        
        heap = []
        
        fuel = startFuel
        prev = 0
        stops = 0
        
        for position, capacity in stations:
            
            distance = position - prev
            
            fuel -= distance
            
            while fuel < 0 and heap:
                fuel += -heapq.heappop(heap)
                stops += 1
            
            if fuel < 0:
                return -1
            
            heapq.heappush(heap, -capacity)
            
            prev = position
        
        # Distance from last station to target
        fuel -= target - prev
        
        while fuel < 0 and heap:
            fuel += -heapq.heappop(heap)
            stops += 1
        
        if fuel < 0:
            return -1
        
        return stops
        