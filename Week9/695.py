class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        stack=[]
        visited=set()
        res=0
        temp=0
        X=[0,1,-1,0]
        Y=[1,0,0,-1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    visited.add((i,j))
                    temp=1
                    stack.append([i,j])
                    while stack:
                        u=stack.pop()
                        for k in range(4):
                            new_x=u[0]+X[k]
                            new_y=u[1]+Y[k]
                            if new_x>=0 and new_y>=0 and new_x<len(grid) and new_y<len(grid[0]) and (new_x,new_y) not in visited and grid[new_x][new_y]==1:
                                temp+=1
                                stack.append([new_x,new_y])
                                visited.add((new_x,new_y))
                
                res=max(res,temp)
        
        return res
                        