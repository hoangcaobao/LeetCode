class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        count1=0
        count2=0
        while count1<len(pushed):
            if len(stack)==0:
                stack.append(pushed[count1])
                count1+=1
            else:
                if stack[-1]==popped[count2]:
                    stack.pop()
                    count2+=1
                else:
                    stack.append(pushed[count1])
                    count1+=1
        
        def check(a,b):
            if a[-1]==b:
                return True
            return False
        
        while count2<len(popped) and check(stack,popped[count2])==True:
            stack.pop()
            count2+=1
        
        return count2==len(popped)