### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def reverse(self, x: int) -> int:
        a=[]
        result=0
        
        if x<0:
            x=abs(x)
            while x>0:
                a.append(x%10)
                x=int(x/10)
            for i in range(0,len(a)):
                result+=a[i]*(10**(len(a)-1-i))
            result=-result
        if x>0:
            while x>0:
                a.append(x%10)
                x=int(x/10)
            for i in range(0,len(a)):
                result+=a[i]*(10**(len(a)-1-i))
        if result<=-(2**31) or result>=(2**31)-1:
            return 0
        return result

