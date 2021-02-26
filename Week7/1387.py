class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            if x==1:
                return 0
            if x%2==0:
                return power(x/2)+1
            else:
                return power(3*x+1)+1
        
        array=[]
        for i in range(lo,hi+1):
            array.append((power(i),i))
        
        array.sort()
        
        return array[k-1][1]