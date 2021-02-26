
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        for i in range(0,len(s)):
            dic[s[i]]=False
        i=0
        j=0
        result=0
        while i<len(s):
            
            if dic[s[i]]==False:
                dic[s[i]]=True
                i+=1
            elif dic[s[i]]!=False:
                result=max(result,i-j)
                dic[s[j]]=False
                j+=1
           
        return max(result,i-j)