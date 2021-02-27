### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
import collections
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
        nums.sort()
        for i in range(0,len(nums)):
            if i+1<len(nums) and nums[i]==nums[i+1]:
                return nums[i]
