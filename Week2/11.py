class Solution:
    def maxArea(self, height: List[int]) -> int:
        result=0
        left=0
        right=len(height)-1
        while left<right:
            a=right-left
            if height[left]>height[right]:
                if result<a*height[right]:
                    result=a*height[right]
                right-=1
            elif height[left]<=height[right]:
                if result<a*height[left]:
                    result=a*height[left]
                left+=1
        return result