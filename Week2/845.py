class Solution:
    def longestMountain(self, A: List[int]) -> int:
        i=0
        j=0
        N=len(A)
        result=0
        while i<N:
            j=i
            if j+1<N and A[j]<A[j+1]:
                while j+1<N and A[j]<A[j+1]:
                    j+=1
                if j+1<N and A[j]>A[j+1]:
                    while j+1<N and A[j]>A[j+1]:
                        j+=1
                    result=max(result,j-i+1)
            i=max(i+1,j)
        return result
                
