class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack1=[]
        stack2=[]
        tamthoi=[]
        
        for i in range(0,len(s)):
            if s[i]==')' or s[i]=='(':
                stack1.append((s[i],i))
            tamthoi.append(s[i])
        while len(stack1)>0:
            if len(stack2)==0:
                stack2.append(stack1[-1])
                stack1.pop()
            else:
                if stack1[-1][0]=='(' and stack2[-1][0]==')':
                    stack2.pop()
                    stack1.pop()
                else:
                    stack2.append(stack1[-1])
                    stack1.pop()
        if len(stack2)>0:
            for i in range(0,len(stack2)):
                del tamthoi[stack2[i][1]]
        result=""
        for i in range(0,len(tamthoi)):
            result+=tamthoi[i]
        return result