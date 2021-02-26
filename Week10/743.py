import heapq
import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph=collections.defaultdict(list)
        heap=[]
        heapq.heapify(heap)
        heapq.heappush(heap,[0,K])
        inf=float('inf')
        dist=[inf for _ in range(N+1)]
        dist[K]=0
        dist[0]=0
        for time in times:
            u,v,w=time
            graph[u].append([w,v])
        while len(heap)>0:
            u=heapq.heappop(heap)
            for ele in graph[u[1]]:
                w=ele[0]
                v=ele[1]
                if w+u[0]<dist[v]:
                    dist[v]=w+u[0]
                    heapq.heappush(heap,[w+u[0],v])

        for i in range(1,len(dist)):
            if dist[i]==inf:
                return -1
            
        
        return max(dist)