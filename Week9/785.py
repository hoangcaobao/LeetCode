import collections
import queue
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        q=queue.Queue()
        visited=[0 for _ in range(len(graph))]
        for i in range(len(graph)):
            if visited[i]==0:
                visited[i]=1
                q.put(i)
                while q.qsize():
                    u=q.get()
                    for v in graph[u]:
                        if visited[v]==0:
                            if visited[u]==1:
                                visited[v]=2
                            else:
                                visited[v]=1
                            q.put(v)
                        else:
                            if visited[v]==visited[u]:
                                return False
        
        return True