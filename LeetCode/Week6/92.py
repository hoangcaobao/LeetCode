# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        current=head
        array=[]
        while current:
            array.append(current.val)
            current=current.next
        i=0
        j=n-1
        current=head
        while current:
            if i>=m-1 and i<=n-1:
                current.val=array[j]
                j-=1
                i+=1
            else:
                current.val=array[i]
                i+=1
            current=current.next
        
        return head
            