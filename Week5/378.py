import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        heapq.heapify(heap)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                heapq.heappush(heap,matrix[i][j])
        
        for i in range(0,k-1):
            heapq.heappop(heap)
        
        return heap[0]
        