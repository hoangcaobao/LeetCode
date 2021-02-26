import queue
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        q=queue.Queue()
        visited=[[False for _ in range(len(board[0]))] for _ in range(len(board))]
        q.put(click)
        visited[click[0]][click[1]]=True
        count=0
        x=[1,-1,0,0,-1,1,-1,1]
        y=[0,0,1,-1,1,1,-1,-1]
        while q.qsize()>0:
            u=q.get()
            for i in range(8):
                new_x=u[0]+x[i]
                new_y=u[1]+y[i]
                if new_x>=0 and new_y>=0 and new_x<len(board) and new_y<len(board[0]) and board[new_x][new_y]=="M":
                    count+=1
                
                
            if count==0 and board[u[0]][u[1]]=="E":
                board[u[0]][u[1]]="B"
                for i in range(8):
                    new_x=u[0]+x[i]
                    new_y=u[1]+y[i]
                    if new_x>=0 and new_y>=0 and new_x<len(board) and new_y<len(board[0]) and visited[new_x][new_y]==False:
                        visited[new_x][new_y]=True
                        q.put([new_x,new_y])
            
            elif count!=0 and board[u[0]][u[1]]=="E":
                board[u[0]][u[1]]=str(count)
            count=0
            
            
            
        if board[click[0]][click[1]]=="M":
            board[click[0]][click[1]]="X"
        
        return board
                