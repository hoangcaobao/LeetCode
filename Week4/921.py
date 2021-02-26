class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack=[]
        array=[]
        for i in range(0,len(S)):
            array.append(S[i])
        while len(array)>0:
            if len(stack)==0:
                stack.append(array[-1])
                array.pop()
            else:
                if stack[-1]==')' and array[-1]=='(':
                    stack.pop()
                    array.pop()
                else:
                    stack.append(array[-1])
                    array.pop()
        
        return len(stack)