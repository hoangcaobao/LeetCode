# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        array=[]
        current=head
        while current:
            heapq.heappush(array,current.val)
            current=current.next
        current=head
        while array:
            x=heapq.heappop(array)
            current.val=x
            current=current.next
        return head