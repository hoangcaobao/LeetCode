### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return nums.index(target) if target in nums else -1 
