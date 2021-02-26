class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        result=[-1]*len(nums)
        n=len(nums)
        for i in range(0,2*n):
            if len(stack)==0:
                stack.append((nums[i%n],i%n))
            else:
                while len(stack)>0 and nums[i%n]>stack[-1][0]:
                    if result[stack[-1][1]]==-1:
                        result[stack[-1][1]]=nums[i%n]
                    stack.pop()
    
                stack.append((nums[i%n],i%n))
        return result