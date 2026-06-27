# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists : return None
        def mergeTwoLists(list1,list2):
            list3=ListNode()
            list3_head=list3
            while list1 and list2:
                if list1.val<list2.val:
                    list3.next=list1
                    list1=list1.next
                else:
                    list3.next=list2
                    list2=list2.next
                list3=list3.next
            if list1:
                list3.next=list1
            if list2:
                list3.next=list2
            return list3_head.next
        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                if i+1<len(lists):
                    merged.append(mergeTwoLists(lists[i],lists[i+1]))
                else:
                    merged.append(lists[i])
            lists=merged
        return lists[0]

               

            
            
