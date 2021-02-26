class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False for _ in range(len(rooms))]
        
        stack=[]
        
        stack.append(rooms[0])
        visited[0]=True
        while stack:
            u=stack.pop()
            for j in u:
                if visited[j]==False:
                    visited[j]=True
                    stack.append(rooms[j])
        
        for i in range(len(rooms)):
            if visited[i]==False:
                return False
        return True