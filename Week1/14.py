class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        position=0
        result=""
        while True:
            if position >= len(strs[0]):
                break
            mark=strs[0][position]
            check=0
            for i in range(1, len(strs)):
                if(position>=len(strs[i])):
                    check=1
                    break
                if(strs[i][position]!=mark):
                    check=1
                    break
            if(check==1):
                break
            result+=mark
            position+=1
        return result
                    
