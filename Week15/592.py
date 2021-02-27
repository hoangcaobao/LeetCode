### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        dau=""
        string=""
        result=[]
        for i in range(0,len(expression)):
            if expression[i] in ["-","+"]:
                if len(result)!=0:
                    result[-1].append(int(string))
                dau=expression[i]
                string=""
            elif expression[i] =="/":
                if dau=="-":
                    result.append([-int(string)])
                    string=""
                    dau=""
                else:
                    result.append([int(string)])
                    string=""
                    dau=""
            else:
                string+=expression[i]
        result[-1].append(int(string))
        mauso=1
        for i in range(0,len(result)):
            mauso*=result[i][1]
        tuso=0
        for i in range(0,len(result)):
            tuso+=(result[i][0]*(mauso//result[i][1]))
        
        uocchung=1
        if tuso==0:
            return "0/1"
        if tuso%mauso==0:
            return "{0}/{1}".format(tuso//mauso,1)
        for i in range(max(tuso,mauso),1,-1):
            
            if tuso%i==0 and mauso%i==0:
                uocchung=i
                break
        
        
        
        
        return "{0}/{1}".format(tuso//uocchung,mauso//uocchung)

