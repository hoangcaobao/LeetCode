import queue
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        array=[]
        q=queue.Queue()
        visited=[[False for _ in range(len(A[0]))] for _ in range(len(A))]
        x=[1,-1,0,0]
        y=[0,0,1,-1]
        for i in range(0,len(A)):
            for j in range(0,len(A[0])):
                if A[i][j]==1:
                    array.append([i,j])
                    q.put([i,j])
                    visited[i][j]=True
                    while q.qsize()>0:
                        
                        for _ in range(q.qsize()):
                            u=q.get()
                            for k in range(4):
                                new_x=u[0]+x[k]
                                new_y=u[1]+y[k]
                                if new_x>=0 and new_y>=0 and new_x<len(A) and new_y<len(A[0]) and visited[new_x][new_y]==False and A[new_x][new_y]==1:
                                    visited[new_x][new_y]=True
                                    array.append([new_x,new_y])
                                    q.put([new_x,new_y])
                    break
            if len(array)!=0:
                break
        
        for i in range(len(array)):
            q.put(array[i])
        count=0
        while q.qsize()>0:
            count+=1
            for _ in range(q.qsize()):
                u=q.get()
                for k in range(4):
                    new_x=u[0]+x[k]
                    new_y=u[1]+y[k]
                    if new_x>=0 and new_y>=0 and new_x<len(A) and new_y<len(A[0]) and visited[new_x][new_y]==False:
                        if A[new_x][new_y]==1:
                            return count-1
                        else:
                            visited[new_x][new_y]=True
                            q.put([new_x,new_y])