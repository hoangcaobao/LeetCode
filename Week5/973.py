import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap=[]
        result=[]
        heapq.heapify(heap)
        for i in points:
            heapq.heappush(heap,[math.sqrt(i[0]**2+i[1]**2),i])
        for i in range(K):
            x=heapq.heappop(heap)
            result.append(x[1])
        return results