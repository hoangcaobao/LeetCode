### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def demso(array):
            left=0
            right=len(array)-1
            count=0
            while left<=right:
                middle=(left+right)//2
                if array[middle]>=0 and middle+1<len(array) and array[middle+1]<0:
                    return len(array)-1-middle
                elif array[middle]>=0:
                    left=middle+1
                elif array[middle]<=0 and middle-1>len(array) and array[middle-1]>0:
                    return len(array)-middle
                else:
                    right=middle-1
            return 0 if array[0]>=0 else len(array)
     
        
        
        self.answer=0    
        for i in range(0,len(grid)):
            self.answer+=demso(grid[i])
        return self.answer
