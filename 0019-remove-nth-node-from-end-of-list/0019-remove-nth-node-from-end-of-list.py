# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        i=head
        j=head
        k=1
        while k<=n:
            k+=1
            i=i.next
        if i is None:
            return head.next
        while i.next is not None:
            i=i.next
            j=j.next
        j.next=j.next.next
        return head
        
        





            
        
        
        