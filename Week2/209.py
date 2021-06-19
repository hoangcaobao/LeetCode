class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        j=0
        tong=0
        res=float('inf')
        for i in range(len(nums)):
            tong+=nums[i]
            while tong>=s and j<len(nums):
                res=min(res,i-j+1)
                
                tong-=nums[j]
                j=j+1
        if res==float('inf'):
            return 0
        return res
