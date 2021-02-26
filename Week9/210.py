def bfs(start, graph, visited, check, array):
    
    for u in graph[start]:
        
        if visited[u]==0:
            visited[u]=1
            array.append(u)
            bfs(u,graph,visited,check,array)
        elif visited[u]==1:
            check['hascycle']=True
        if array.index(start)>array.index(u):
            array.remove(start)
            array.insert(array.index(u),start)
        visited[u]=2
import collections
import queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        check={'hascycle':False}
        visited=[0 for _ in range(numCourses)]
        graph=collections.defaultdict(list)
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        array=[]

        for i in range(numCourses):
            if visited[i]==0:
                visited[i]=1
                array.append(i)

                bfs(i, graph,visited,check,array)

                visited[i]=2
       




        if check['hascycle']==True:
            return []
        return array