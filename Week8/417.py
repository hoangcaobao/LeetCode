import queue
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        visited_pacific=set()
        visited_atlantic=set()
        pacific=queue.Queue()
        atlantic=queue.Queue()
        if not matrix:
            return
        for i in range(0,len(matrix[0])):
            pacific.put([0,i])
        for i in range(0,len(matrix)):
            pacific.put([i,0])
        for i in range(0,len(matrix[0])):
            atlantic.put([len(matrix)-1,i])
        for i in range(0,len(matrix)):
            atlantic.put([i,len(matrix[0])-1])
        def bfs(q,visited,matrix):
            x=[0,0,1,-1]
            y=[1,-1,0,0]
            while q.qsize()>0:
                u=q.get()
                if (u[0],u[1]) in visited:
                    continue
                visited.add((u[0],u[1]))
                for i in range(4):
                    new_x=u[0]+x[i]
                    new_y=u[1]+y[i]
                    if new_x>=0 and new_y>=0 and new_x<len(matrix) and new_y<len(matrix[0])  and matrix[new_x][new_y]>=matrix[u[0]][u[1]]:
                        q.put([new_x,new_y])
                        
        
        bfs(pacific,visited_pacific,matrix)
        bfs(atlantic,visited_atlantic,matrix)
        return visited_pacific&visited_atlantic