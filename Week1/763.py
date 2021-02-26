import collections
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic=collections.defaultdict(list)
        for i in range(0,len(S)):
            dic[S[i]].append(i)
        i=0
        check=[]
        result=[]
        while i<len(S):
            
            chan=dic[S[i]][-1]
            for key in dic:
                if dic[key][0]<chan and dic[key][-1]>chan:
                    chan=dic[key][-1]
                    
                    
            
            result.append(chan-i+1)
            i=chan+1
        return result
            