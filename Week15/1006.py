### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def clumsy(self, N: int) -> int:
        res=[]
        danhanvachiachua=False
        i=N
        while i>0:
            if danhanvachiachua==False:
                if i>=3:
                    res.append((i*(i-1))//(i-2))
                elif i==2:
                    res.append(2)
                elif i==1:
                    res.append(1)
                i=i-3
                danhanvachiachua=True
            else:
                res.append(i)
                i=i-1
                danhanvachiachua=False
                
            
        print(res)
        dau=0
        clumsy=res[0]
        for i in range(1,len(res)):
            if dau%2==0:
                clumsy+=res[i]
            else:
                clumsy-=res[i]
            dau+=1
        return clumsy

