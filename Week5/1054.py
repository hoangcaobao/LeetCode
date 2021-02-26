import heapq
import collections
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dic=collections.defaultdict(int)
        heap=[]
        heapq.heapify(heap)
        for i in barcodes:
            dic[i]+=1
        for key in dic:
            heapq.heappush(heap,[-dic[key],key])
        result=[]
        while len(heap)>0:
            x1=heapq.heappop(heap)
            fre=-x1[0]
            val=x1[1]
            if len(result)==0 or result[-1]!=val:
                result.append(val)
                fre-=1
                if fre>0:
                    heapq.heappush(heap,[-fre,val])
            else:
                x2=heapq.heappop(heap)
                heapq.heappush(heap,[-fre,val])
                fre=-x2[0]
                val=x2[1]
                result.append(val)
                fre-=1
                if fre>0:
                    heapq.heappush(heap,[-fre,val])
        return result
            