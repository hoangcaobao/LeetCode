class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        stack=[]
        visited=set()
        x=[1,-1,0,0]
        y=[0,0,1,-1]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp=0
                if grid[i][j]==0 and (i,j) not in visited:
                    stack.append([i,j])
                    visited.add((i,j))
                    if i==0 or i==len(grid)-1 or j==0 or j==len(grid[0])-1:
                        temp=0
                    else:
                        temp=1
                    while stack:
                        u=stack.pop()
                        for k in range(4):
                            new_x=u[0]+x[k]
                            new_y=u[1]+y[k]
                            if new_x>=0 and new_y>=0 and new_x<len(grid) and new_y<len(grid[0]) and grid[new_x][new_y]==0 and (new_x,new_y) not in visited:
                                stack.append([new_x,new_y])
                                visited.add((new_x,new_y))
                                if new_x==0 or new_x==len(grid)-1 or new_y==0 or new_y ==len(grid[0])-1:
                                    temp=0
                count+=temp
        return count