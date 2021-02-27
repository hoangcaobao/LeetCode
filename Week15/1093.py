### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        sosohang=0
        sobenhat=0
        solonnhat=0
        tong=0
        for i in range(0,len(count)):
            if count[i]!=0:
                sobenhat=i
                break
        for i in range(len(count)-1,-1,-1):
            if count[i]!=0:
                solonnhat=i
                break
        mode=0
        for i in range(0,len(count)):
            sosohang+=count[i]
            if count[i]>count[mode]:
                mode=i
            tong+=(count[i]*i)
        dem=0
        print(sosohang)
        print(tong)
        mean=tong/sosohang
        if sosohang%2==0:
            vitri1=sosohang//2
            vitri1_bool=False
            vitri2=sosohang//2+1
            vitri2_bool=False
            median=0
            
            for i in range(0,len(count)):
                dem+=count[i]
                if vitri2_bool==True and vitri1_bool==True:
                    break
                if dem>=vitri1 and vitri1_bool==False:
                    median+=i
                    
                    vitri1_bool=True
                if dem>=vitri2 and vitri2_bool==False:
                    median+=i
                    
                    vitri2_bool=True
                
            
            return [float(sobenhat),float(solonnhat),float(mean),float(median/2),float(mode)]
        else:
            median=0
            
            for i in range(0,len(count)):
                dem+=count[i]
                if dem>=(sosohang//2+1):
                    median+=i
                   
                    break
            
            return [float(sobenhat),float(solonnhat),float(mean),float(median),float(mode)]

