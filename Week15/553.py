### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums)==1:
            return "{}".format(nums[0])
        elif len(nums)==2:
            return "{0}/{1}".format(nums[0],nums[1])
        res=""
        res+=str(nums[0])
        res+="/"
        res+="("
        res+=str(nums[1])
        for i in range(2,len(nums)):
            res+="/"
            res+=str(nums[i])
        
        
        res+=")"
        return res

