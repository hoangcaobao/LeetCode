### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour=(hour/12+(1/12)*(minutes/60))
        while hour>1:
            hour=hour-1
        print(hour)
        minutes=minutes/60
        print(minutes)
        
        result=(abs(hour-minutes)*360)%360
        if result>180:
            return 360-result
        else:
            return result
        

