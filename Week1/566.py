class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        new_matrix=[[0 for _ in range (c)] for _ in range (r)]
        if r*c!=len(nums)*len(nums[0]):
            return nums
        i1=0
        j1=0
        for j in range(0,len(nums)):
            for i in range(0,len(nums[0])):
                if i1==c:
                    i1=0
                    j1+=1
                if j1<r:
                    new_matrix[j1][i1]=nums[j][i]
                    i1+=1
        return new_matrix