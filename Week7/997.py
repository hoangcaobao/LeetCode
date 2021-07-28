class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        graph=[[] for _ in range(N)]
        for t in trust:
            graph[t[0]-1].append(t[1])
        count=0
        townjudge=0
        for i in range(N):
            if len(graph[i])==0:
                townjudge=i+1
                count+=1
        if count!=1:
            return -1
        count=0
        for i in range(N):
            if len(graph[i])!=0:
                for j in graph[i]:
                    if j==townjudge:
                        count+=1
                        break
                       
                
                if count!=1:
                    return -1
                count=0
        
        return townjudge
