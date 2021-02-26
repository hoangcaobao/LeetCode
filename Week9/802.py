def dfs(start,visited,graph):
    if visited[start]!=0:
        return visited[start]==2
    visited[start]=1
    for i in graph[start]:
        
        if visited[i]==1 or not dfs(i,visited,graph):
            return False
    visited[start]=2
    return True
            
    
    
import collections            
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited=[0 for _ in range(len(graph))]
        array=[False for _ in range(len(graph))]
        for i in range(0,len(graph)):
            array[i]=dfs(i,visited,graph)
        res=[]
        for i in range(len(graph)):
            if array[i]==True:
                res.append(i)
        return res
            