### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N==0:
            return"0"
        count = 0
        res=[]
        
        while N > 0:
            if count%2==0:
                d=2
            else:
                d=-2
            
            remain = N % d
            N //= d
            N = abs(N)
            res.append(str(abs(remain)))
            count+=1
            
        res.reverse()
        return "".join(res)

