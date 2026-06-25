# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=n
        fast=head
        slow=head
        while count!=0:
            fast=fast.next
            count-=1
        if not fast:
            return head.next
        fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        temp=slow.next.next if slow.next else None
        slow.next=temp
        return head if head else slow

