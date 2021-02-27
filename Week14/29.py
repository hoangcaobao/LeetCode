### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        if dividend/divisor<0:
            return dividend//divisor if dividend%divisor==0 else dividend//divisor +1
        else:
            return dividend//divisor
        
