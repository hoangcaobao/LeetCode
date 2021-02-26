from fractions import Fraction
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        array=[]
        for i in range(0,len(quality)):
            array.append((Fraction(wage[i],quality[i]),quality[i],wage[i]))
        array.sort()
        result=100000000000000000000000000000
        heap=[]
        heapq.heapify(heap)
        tong_quality=0
        for tyle, q, w, in array:
            heapq.heappush(heap,-q)
            tong_quality+=q
            if len(heap)>K:
                tong_quality+=heapq.heappop(heap)
            if len(heap)==K:
                result=min(result,tyle*tong_quality)
        
        return float(result)