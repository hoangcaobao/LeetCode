class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited=[False for _ in range(len(arr))]
        stack=[]
        if arr[start]==0:
            return True
        stack.append([arr[start],start])
        visited[start]=True
        while stack:
            u=stack.pop()
            plus=u[0]+u[1]
            minus=u[1]-u[0]
            if plus>=0 and plus<len(arr) and visited[plus]==False:
                if arr[plus]==0:
                    return True
                visited[plus]=True
                
                stack.append([arr[plus],plus])
            if minus>=0 and minus<len(arr) and visited[minus]==False:
                if arr[minus]==0:
                    return True
                visited[minus]=True
                stack.append([arr[minus],minus])
        return False