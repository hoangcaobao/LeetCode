### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
import math
class Solution:
    def numSquares(self, n: int) -> int:
        squares=[i**2 for i in range(1,int(math.sqrt(n))+1)]
        dp=[float("inf")]*(n+1)
        dp[0]=0
        for i in range(1,len(dp)):
            for square in squares:
                if i-square<0:
                    break
                else:
                    dp[i]=min(dp[i],dp[i-square]+1)
        
        return dp[-1]

