class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        parent=[i for i in range(len(M))]
        rank=[0 for i in range(len(M))]
        def findset(u,parent):
            if parent[u]!=u:
                parent[u]=findset(parent[u],parent)
            return parent[u]
        def unionbyrank(u,v,rank,parent):
            u_parent=findset(u,parent)
            v_parent=findset(v,parent)
            if u_parent==v_parent:
                return
            if rank[u_parent]>rank[v_parent]:
                parent[v_parent]=u_parent
            elif rank[u_parent]<rank[v_parent]:
                parent[u_parent]=v_parent
            else:
                parent[v_parent]=u_parent
                rank[u_parent]+=1
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j]==1:
                    unionbyrank(i,j,rank,parent)
        count=0 
        for i in range(len(parent)):
            if parent[i]==i:
                count+=1
        return count  
