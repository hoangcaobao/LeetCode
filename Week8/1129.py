import collections
import queue
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        q=queue.Queue()
        visitedred=[False]*n
        visitedblue=[False]*n
        
        visitedred[0]=True
        visitedblue[0]=True
        res=[float('inf')]*n
        res[0]=0
        graph_red=collections.defaultdict(list)
        graph_blue=collections.defaultdict(list)
        for red_edge in red_edges:
            u,v=red_edge
            graph_red[u].append(v)
        
        for blue_edge in blue_edges:
            u,v=blue_edge
            graph_blue[u].append(v)
        
        q.put([0,"RED"])
        q.put([0,"BLUE"])
        count=0
        while q.qsize()>0:
            count+=1
            
            for j in range(0,q.qsize()):
                u=q.get()
                if u[1]=="RED":
                    for v in graph_red[u[0]]:
                        
                        if visitedred[v]==False:
                            q.put([v,"BLUE"])
                            visitedred[v]=True
                            res[v]=min(count,res[v])
                    
                        
                else:    
                    for v in graph_blue[u[0]]:
                        
                        if visitedblue[v]==False :
                            q.put([v,"RED"])
                            visitedblue[v]=True
                            res[v]=min(count,res[v])
        
        for i in range(len(res)):
            if res[i]==float('inf'):
                res[i]=-1
                
                    
        res[0]=0
        return res