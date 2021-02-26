# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        nhohonx=a=ListNode(0)
        lonhonx=b=ListNode(0)
        while head:
            if head.val<x:
                nhohonx.next=head
                nhohonx=nhohonx.next
                head=head.next
            else:
                lonhonx.next=head
                lonhonx=lonhonx.next
                head=head.next
        
        lonhonx.next=None
        nhohonx.next=b.next
        return a.next
                