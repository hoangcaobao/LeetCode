### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles)==1:
            return piles[0]//H +1 if piles[0]%H else piles[0]//H
        left=max(piles)//(H-(len(piles)-1))
        right=max(piles)
        
        def isok(piles,n,H):
            count=0
            for i in range(0,len(piles)):
                if count>H:
                    return False
                if piles[i]%n==0:
                    count+=(piles[i]//n)
                else:
                    count+=((piles[i]//n)+1)
            return count<=H
        
        
        
        while left<=right:
            middle=(left+right)//2
           
            if isok(piles,middle,H):
                right=middle-1
                
            else:
                left=middle+1
            print([left,right])
            
        
        return left
                    
