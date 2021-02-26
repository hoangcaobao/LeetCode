import queue
def bfs(start, destination, graph,visited):
    q=queue.Queue()
    q.put(start)
    visited[start]=1
    while q.qsize()>0:
        u=q.get()
        if u==destination:
            return True
        if destination in graph[u]:
            return True
        for v in graph[u]:
            if v==destination:
                return True
            if visited[v]==0:
                visited[v]=1
                q.put(v)
                if v not in graph[start]:
                    graph[start].append(v)
    
import collections
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=collections.defaultdict(list)
        for i in prerequisites:
            graph[i[1]].append(i[0])
        visited=[0 for _ in range(n)]
        
        array=[]
        res=[False for i in range(len(queries))]
        for i in range(len(queries)):
            res[i]=  bfs(queries[i][1],queries[i][0],graph,visited)
            visited=[0 for _ in range(n)]
        
        return res