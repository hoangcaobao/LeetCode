import queue
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        q=queue.Queue()
        if len(grid)==1 and len(grid[0])==  1:
            return True
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        visited[0][0]=True
        q.put([grid[0][0],0,0])
        def check(x,y,limit_x,limit_y):
            if x>=0 and y>=0 and x<limit_x and y<limit_y:
                return True
            return False
        while q.qsize()>0:
            u=q.get()
            if u[0]==1:
                new_x=u[1]
                new_y=u[2]+1
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==3 or grid[new_x][new_y]==5 or grid[new_x][new_y]==1) :
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
                
                new_x=u[1]
                new_y=u[2]-1
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==4 or grid[new_x][new_y]==6 or grid[new_x][new_y]==1):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
            
            elif u[0]==2:
                new_x=u[1]+1
                new_y=u[2]
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==5 or grid[new_x][new_y]==6 or grid[new_x][new_y]==2) :
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
                new_x=u[1]-1
                new_y=u[2]
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==3 or grid[new_x][new_y]==4 or grid[new_x][new_y]==2):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
            
            elif u[0]==3:
                new_x=u[1]+1
                new_y=u[2]
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==2 or grid[new_x][new_y]==6 or grid[new_x][new_y]==5):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
                new_x=u[1]
                new_y=u[2]-1
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==1 or grid[new_x][new_y]==4 or grid[new_x][new_y]==6):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
            elif u[0]==4:
                new_x=u[1]+1
                new_y=u[2]
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==2 or grid[new_x][new_y]==6 or grid[new_x][new_y]==5):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
                new_x=u[1]
                new_y=u[2]+1
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==1 or grid[new_x][new_y]==3 or grid[new_x][new_y]==5):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
            elif u[0]==5:
                new_x=u[1]
                new_y=u[2]-1
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==1 or grid[new_x][new_y]==6 or grid[new_x][new_y]==4):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
                new_x=u[1]-1
                new_y=u[2]
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==2 or grid[new_x][new_y]==3 or grid[new_x][new_y]==4):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
            elif u[0]==6:
                new_x=u[1]
                new_y=u[2]+1
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==1 or grid[new_x][new_y]==3 or grid[new_x][new_y]==5):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
                new_x=u[1]-1
                new_y=u[2]
                if check(new_x,new_y,len(grid),len(grid[0]))==True and visited[new_x][new_y]==False and (grid[new_x][new_y]==2 or grid[new_x][new_y]==3 or grid[new_x][new_y]==4):
                    if new_x==len(grid)-1 and new_y==len(grid[0])-1:
                        return True
                    q.put([grid[new_x][new_y],new_x,new_y])
                    visited[new_x][new_y]=True
            
        return False