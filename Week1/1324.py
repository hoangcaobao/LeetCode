class Solution:
    def printVertically(self, s: str) -> List[str]:
        x=s.split(" ")
        dodailonnhat=0
        result=[]
        chu=""
        
        for i in range(0,len(x)):
            if len(x[i])>dodailonnhat:
                dodailonnhat=len(x[i])
        for i in range(0,len(x)):
            x[i]+=((dodailonnhat-len(x[i]))*" ")
            
        for i in range(0,len(x)):
            if len(x[i])>dodailonnhat:
                dodailonnhat=len(x[i])
        for i in range(0,dodailonnhat):
            for j in range(0,len(x)):
                chu+=x[j][i]
            result.append(chu)
            chu=""
        for i in range(0,len(result)):
            result[i]=result[i].rstrip()
                
        return result
