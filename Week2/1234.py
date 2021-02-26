import collections
class Solution:
    def balancedString(self, s: str) -> int:
       
        dic=collections.defaultdict(int)
        for i in range(0,len(s)):
            dic[s[i]]+=1
        for key in dic:
            if dic[key]>int(len(s)/4):
                dic[key]-=int(len(s)/4)
            else:
                dic[key]=0
        for i in range(0,len(s)):
            if dic[s[i]]==0:
                del dic[s[i]]

        def checkloi(dic):
            for key in dic:
                if dic[key]>0:
                    return False
            return True
        
        j=0
        result=len(s)+1
        for i in range(0,len(s)) :
        
            
            if s[i] in dic:
                dic[s[i]]-=1
            
                while checkloi(dic)==True :
                    result=min(result,i-j+1)

                    if s[j] in dic:
                        dic[s[j]]+=1
                    j+=1
        
        return result%(len(s)+1)