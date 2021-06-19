import collections
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dic={0:[]}
        if len(nums)==1:
            return True
        for i in range(0,len(nums)):
            if nums[i]==0:
                dic[0].append(i)
        if len(dic[0])==0:
            return True
        if dic[0][-1]==len(nums)-1:
            dic[0].pop()
        i=0
        count=0
        while i<len(nums):
            if count==len(dic[0]):
                return True
            if i>=dic[0][count]:
                return False
            if nums[i]>(dic[0][count]-i) :
                count+=1
                i-=1
            
            i+=1
        return False
