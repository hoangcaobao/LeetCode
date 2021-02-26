class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
 
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                tong=nums[i]+nums[left]+nums[right]
                if tong==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while   nums[left]==nums[left-1] and left<right:
                        left+=1
                else:
                    if tong<0:
                        left+=1
                    if tong>0:
                        right-=1
        
        return result