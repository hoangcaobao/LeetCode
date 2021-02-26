# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=ListNode(0)
        current=res
        while l1 and l2:
            if l1.val<=l2.val:
                current.next=l1
                l1=l1.next
                current=current.next
               
                
            else:
                current.next=l2
                l2=l2.next
                current=current.next
                
        
        if l1:
            current.next=l1
        else:
            current.next=l2
        
        