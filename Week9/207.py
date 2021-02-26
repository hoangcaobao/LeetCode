def dfs(start,check,visited,graph):
    
    for v in graph[start]:
        if visited[v]==0:
            visited[v]=1
            dfs(v,check,visited,graph)
        elif visited[v]==1:
            check['hascycle']=True
        
        visited[v]=2
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        check={"hascycle": False}
        visited=[0 for _ in range(numCourses)]
        graph=collections.defaultdict(list)
        
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        
        for i in range(numCourses):
            visited[i]=1
            dfs(i,check,visited,graph)
            visited[i]=2
        
        if check['hascycle']==True:
            return False
        for i in range(numCourses):
            if visited[i]==0:
                return False
        return True
        