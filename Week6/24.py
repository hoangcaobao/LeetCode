# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        count1=0
        current=head
        if not current:
            return head
        while current.next:
            if count1%2==0:
                current.val,current.next.val=current.next.val,current.val
            count1+=1
            current=current.next
        return head
        