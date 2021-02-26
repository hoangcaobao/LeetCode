class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        rank=[0 for i in range(n)]
        def findpath(u,parent):
            if parent[u]!=u:
                parent[u]=findpath(parent[u],parent)
            return parent[u]
        def unionrank(u,v,rank,parent):
            u_parent=findpath(u,parent)
            v_parent=findpath(v,parent)
            if u_parent==v_parent:
                return
            if rank[u_parent]>rank[v_parent]:
                parent[v_parent]=u_parent
            elif rank[u_parent]<rank[v_parent]:
                parent[u_parent]=v_parent
            else:
                parent[u_parent]=v_parent
                rank[v_parent]+=1
        
        for connection in connections:
            u,v=connection
            unionrank(u,v,rank,parent)
   
        count=0
        for i in range(len(parent)):
            if parent[i]==i:
                count+=1
        if len(connections)<n-1:
            return -1
        
        
        
        return count-1