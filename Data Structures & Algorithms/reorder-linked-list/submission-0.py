# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        counthead=head
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        fast=slow.next
        slow.next=None
        prev=None
        while fast:
            temp=fast.next
            fast.next=prev
            prev=fast
            fast=temp
        fast=head
        slow=prev
        while slow:
            temp1=fast.next
            temp2=slow.next
            fast.next=slow
            slow.next=temp1
            fast=temp1
            slow=temp2







        