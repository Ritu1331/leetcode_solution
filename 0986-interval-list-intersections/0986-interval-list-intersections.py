class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        n = len(firstList)
        m = len(secondList)
        i,j=0,0
        s,e=0,0

        while(i<n and j<m):
            start1, end1 = firstList[i]
            start2,end2 = secondList[j]

            
            s=max(start1,start2)
            e = min(end1,end2)

            if (s<=e):
                res.append([s,e])
            
            if(end1<=end2):
                i+=1
            else:
                j+=1
        return res
                     
            


        
        
        