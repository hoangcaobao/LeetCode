class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack1=[]
        stack2=[]
        for i in range(0,len(S)):
            stack1.append([S[i],False,0])
        result=0
        
        while len(stack1)>0:
            if len(stack2)==0:
            
                stack2.append(stack1[-1])
                stack1.pop()
            else:
                if len(stack2)>1:
                    if stack1[-1][0]=='(' and stack2[-1][0]==')' and stack2[-1][1]==False:
                        
                        stack2.pop()
                        stack1.pop()
                        stack2[-1][2]+=1
                    elif stack1[-1][0]=='(' and stack2[-1][0]==')' and stack2[-1][1]==True:
                        stack2[-2][2]+=(stack2[-1][2]*2)
                        stack2.pop()
                        stack1.pop()
                    else:
                        stack2.append(stack1[-1])
                        stack2[-2][1]=True
                        stack1.pop()
                else:
                    if stack1[-1][0]=='(' and stack2[-1][0]==')' and stack2[-1][1]==False:
                        result+=1
                        stack1.pop()
                        stack2.pop()
                    elif stack1[-1][0]=='(' and stack2[-1][0]==')' and stack2[-1][1]==True:
                        result+=(stack2[-1][2]*2)
                        stack1.pop()
                        stack2.pop()
                    else:
                        stack2.append(stack1[-1])
                        stack2[-2][1]=True
                        stack1.pop()
                        
                        
        
        return result
                    