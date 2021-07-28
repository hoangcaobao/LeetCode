import collections
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph={
            
        }
        graph=collections.defaultdict(list)
        for path in paths:
            graph[path[0]].append(path[1])
            graph[path[1]].append(path[0])
            
        res=[0]*(N+1)
        
        used=[False]*5
        for i in range(1,N+1):
            
            for j in graph[i]:
                
                    
                used[res[j]]=True
            
            for j in range(1,5):
                if used[j]==False:
                    res[i]=j
                    break
            
            used=[False]*5
            
        
                    
        
        
        res.pop(0)
        return res
