class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
       
        n = len(citations)

        low = 0
        high = n - 1

        while low <= high:

            mid = (low + high) // 2

            papers = n - mid

            if citations[mid] == papers:
                return papers

            elif citations[mid] < papers:
                low = mid + 1

            else:
                high = mid - 1

        return n - low
            
        