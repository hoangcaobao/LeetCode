class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack1=[]
        stack2=[]
        for i in S:
            stack1.append(i)
        while len(stack1)>0:
            if len(stack2)==0:
                stack2.append(stack1[-1])
                stack1.pop()
            else:
                if stack1[-1]==stack2[-1]:
                    stack2.pop()
                    stack1.pop()
                else:
                    stack2.append(stack1[-1])
                    stack1.pop()
        result=""
        for i in range(len(stack2)-1,-1,-1):
            result+=stack2[i]
        return result