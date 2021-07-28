import heapq
import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph=collections.defaultdict(list)
        for flight in flights:
            u,v,w=flight
            graph[u].append([w,v])
        heap=[]
        inf=float('inf')
        dist=[inf for _ in range(n+1)]
        dist[src]=0
        
        heapq.heappush(heap,[0,0,src])
        while len(heap)>0:
            u=heapq.heappop(heap)
            for ele in graph[u[2]]:
                w=ele[0]
                v=ele[1]
                if w+u[1]<dist[v] and u[0]<=K:
                    dist[v]=w+u[1]
                    heapq.heappush(heap,[u[0]+1,u[1]+w,v])
        if dist[dst]==inf:
            return -1
        else:
            return dist[dst]
        
