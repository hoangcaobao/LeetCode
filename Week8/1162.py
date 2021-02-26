import collections
import queue
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N=len(grid)
        if N==0:
            return -1
        q=queue.Queue()
        for i in range(N):
            for j in range(N):
                if grid[i][j]==1:
                    q.put([i,j,0])
        visited=[[False for _ in range(N)] for _ in range(N)]
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        maxDistance=0
        while q.qsize():
            u=q.get()
            maxDistance=max(maxDistance,u[2])
            for i in range(4):
                new_x=u[0]+x[i]
                new_y=u[1]+y[i]
                if new_x>=0 and new_y>=0 and new_x<N and new_y<N and visited[new_x][new_y]==False and grid[new_x][new_y]==0:
                    visited[new_x][new_y]=True
                    q.put([new_x,new_y,u[2]+1])
        
        return maxDistance or -1