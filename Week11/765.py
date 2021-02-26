class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        parent=[i for i in range(len(row))]
        for i in range(1,len(row),2):
            parent[i]-=1
        
        def findpath(u,parent):
            if parent[u]!=u:
                parent[u]=findpath(parent[u],parent)
            return parent[u]
        for i in range(0,len(row),2):
            u_parent=findpath(row[i],parent)
            v_parent=findpath(row[i+1],parent)
          
            parent[u_parent]=v_parent
    

        return (len(row)//2)-sum([1 for i in range(0,len(row),2) if parent[i]==parent[i+1]==i])
        