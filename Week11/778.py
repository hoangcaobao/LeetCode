class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        marked=float('inf')
        x=[1,-1,0,0]
        y=[0,0,1,-1]
        stack=[]
        visited=[[float('inf') for _ in range(len(grid[0]))]for _ in range(len(grid))]
        stack.append([0,0])
        visited[0][0]=grid[0][0]
        
        while stack:
            u=stack.pop()
            for i in range(4):
                new_x=u[0]+x[i]
                new_y=u[1]+y[i]
                if new_x>=0 and new_y>=0 and new_x<len(grid) and new_y<len(grid[0]) and max(grid[new_x][new_y],visited[u[0]][u[1]])<visited[new_x][new_y]:
                    visited[new_x][new_y]=max(grid[new_x][new_y],visited[u[0]][u[1]])
                    stack.append([new_x,new_y])
        
        return visited[-1][-1]