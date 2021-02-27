### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
import math
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res=[]
        differnet=0
        
        for i in range(int(math.sqrt(num+1))+1,0,-1):
            if (num+1)%i==0:
                res.append(i)
                res.append((num+1)//i)
                different=abs((num+1)//i-i)
                
                break
        
        for i in range(int(math.sqrt(num+2))+1,0,-1):
            if (num+2)%i==0:
                if different>abs((num+2)//i-i):
                    res.pop()
                    res.pop()
                    res.append(i)
                    res.append((num+2)//i)
                break
        
        return res

