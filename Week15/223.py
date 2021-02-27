### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left = max(A, E)
        right = min(C, G)
        
        top = min(D, H)
        bottom = max(B, F)
        
        
        area_1 = (C - A)*(D - B)
        area_2 = (G - E)*(H - F)
        
        if (left < right) and (bottom < top):
            
            giaonhau = ( right - left ) * ( top - bottom )
			
        else:
            giaonhau = 0
        
        return area_1 + area_2 - giaonhau

