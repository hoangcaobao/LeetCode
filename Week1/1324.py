class Solution:
    def printVertically(self, s: str) -> List[str]:
        result=""
        mang=[]
        for i in range(len(s)):
            if s[i]!=" ":
                result+=s[i]
            else:
                mang.append(result)
                result=""
        mang.append(result)
        return mang