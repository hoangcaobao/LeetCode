import collections
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic=collections.defaultdict(int)
        for i in words:
            dic[i]+=1
        heap=[]
        heapq.heapify(heap)
        for key in dic:
            heapq.heappush(heap,[-dic[key],key])
        result=[]
        for i in range(0,k):
            x=heapq.heappop(heap)
            result.append(x[1])
        return result