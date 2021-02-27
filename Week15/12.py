### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def intToRoman(self, num: int) -> str:
        sodukhichiacho5={
            1:"I",
            2:"X",
            3:"C",
            4:"M",
        }
        chiahetcho5={
            1:"V",
            2:"L",
            3:"D",
        }
        a=str(num)
        j=len(a)
        while num%10==0:
            num=num//10
        a=str(num)
        res=""
        for i in range(0,len(a)):
            if a[i]=="9":
                res+=sodukhichiacho5[j-i]
                res+=sodukhichiacho5[j-i+1]
            elif a[i]=="4":
                res+=sodukhichiacho5[j-i]
                res+=chiahetcho5[j-i]
        
            elif int(a[i])//5==1:
                res+=chiahetcho5[j-i]
                res+=sodukhichiacho5[j-i]*(int(a[i])-5)
            else:
                print(a[i])
                res+=sodukhichiacho5[j-i]*int(a[i])
      
            
        
        return res

