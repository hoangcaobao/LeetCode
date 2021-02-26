
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        array=[]
        current=head
        while current:
            array.append(current.val)
            current=current.next
        
        stack=[]
        res=[0]*len(array)
        for i in range(0,len(array)):  
            while stack and array[i]>stack[-1][0]:
                res[stack[-1][1]]=array[i]
                stack.pop()
            stack.append((array[i],i))
        
        # current=head
        # i=0
        # while current:
        #     current.val=res[i]
        #     i+=1
        #     current=current.next
        # return head
        
        return res
        