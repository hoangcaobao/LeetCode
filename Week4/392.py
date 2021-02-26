class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count=0
        if s=="" :
            return True
        if t=="":
            return False
        for i in range (0,len(t)):
            if count<len(s) and s[count]==t[i]:
                count+=1
        if count<len(s):
            return False
        return True
        