import queue
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N=len(board)
        def hangvacot(S):
            if S%N==0:
                if int(S/N)%2!=0:
                    return N-int(S/N),N-1
                else:
                    return N-int(S/N),0
            
            else:
                if (S//N)%2==0:
                    return N-1-(S//N),S%N-1
                else:
                    return N-1-(S//N),N-S%N
                
        visited=[False for _ in range(N*N+1)]
        
        q=queue.Queue()
        q.put(1)
        answer=[]
        count=0
        while q.qsize()>0:
            count+=1
            for _ in range(q.qsize()):
                u=q.get()
                if u+6>=N*N:
                    return count
                for i in range(u+1,u+7):
                    
                    if visited[i]==False:

                        visited[i]=True
                        r,c=hangvacot(i)

                        if board[r][c]==-1:
                            q.put(i)
                        else:
                            if board[r][c]==N*N:
                                return count
                            q.put(board[r][c])
        return -1