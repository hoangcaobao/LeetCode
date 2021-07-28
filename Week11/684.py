class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        rank=[0 for i in range(len(edges)+1)]
        def findpath(u,parent):
            if parent[u]!=u:
                parent[u]=findpath(parent[u],parent)
            return parent[u]
        
        for edge in edges:
            u,v=edge
            u_parent=findpath(u,parent)
            v_parent=findpath(v,parent)
            if u_parent==v_parent:
                return edge
            if rank[u_parent]>rank[v_parent]:
                parent[v_parent]=u_parent
            elif rank[u_parent]<rank[v_parent]:
                parent[u_parent]=v_parent
            else:
                parent[u_parent]=v_parent
                rank[v_parent]+=1
