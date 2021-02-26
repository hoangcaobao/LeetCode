class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count={}
        rank={}
        parent={}
        for num in nums:
            count[num]=1
            rank[num]=0
            parent[num]=num
        
        def findpath(u,parent):
            if parent[u]!=u:
                parent[u]=findpath(parent[u],parent)
            return parent[u]
    
        def union(u,v,rank,parent):
            if v not in parent:
                return
            u_parent=findpath(u,parent)
            v_parent=findpath(v,parent)
            if u_parent==v_parent:
                return 
            if rank[u_parent]>rank[v_parent]:
                parent[v_parent]=u_parent
                count[u_parent]+=count[v_parent]
            elif rank[u_parent]<rank[v_parent]:
                parent[u_parent]=v_parent
                count[v_parent]+=count[u_parent]
            else:
                parent[u_parent]=v_parent
                count[v_parent]+=count[u_parent]
                rank[v_parent]+=1
        
        for num in nums:
            union(num,num+1,rank,parent)
            union(num,num-1,rank,parent)
     
        array=[] 
        for num in nums:
            if parent[num]==num:
                array.append(count[num])
        if len(array)==0:
            return 0
        return max(array)   