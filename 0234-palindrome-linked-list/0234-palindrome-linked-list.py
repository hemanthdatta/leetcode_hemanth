# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #lets do two pointer method
        def reverse(head):
            p=None
            c=head
            while c is not None:
                n=c.next
                c.next=p
                p=c
                c=n
            return p
        if head is None or head.next is None:
            return True
        
        slow=head
        fast=head
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        rev=reverse(slow)

        while rev is not None:
            if head.val != rev.val:
                return False
                break
            head=head.next
            rev=rev.next
        return True


        

        
        

        