class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack=[]
        visited=set()
        x=[1,-1,0,0]
        y=[0,0,1,-1]
        array=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp=0
                if board[i][j]=="O" and (i,j) not in visited:
                    stack.append([i,j])
                    visited.add((i,j))
                    array.append([i,j])
                    if i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1:
                        temp=0
                    else:
                        temp=1
                    while stack:
                        u=stack.pop()
                        for k in range(4):
                            new_x=u[0]+x[k]
                            new_y=u[1]+y[k]
                            if new_x>=0 and new_y>=0 and new_x<len(board) and new_y<len(board[0]) and board[new_x][new_y]=="O" and (new_x,new_y) not in visited:
                                array.append([new_x,new_y])
                                stack.append([new_x,new_y])
                                visited.add((new_x,new_y))
                                if new_x==0 or new_x==len(board)-1 or new_y==0 or new_y ==len(board[0])-1:
                                    temp=0
                
                if temp==1:
                    for u in array:
                        board[u[0]][u[1]]="X"
                array=[]