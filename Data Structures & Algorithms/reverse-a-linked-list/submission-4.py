# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None 
        while curr:
            tmp = curr.next 
            print("curr value: ", curr.val)
            curr.next = prev 
            #print("curr.next val: ", curr.next.val)
            prev = curr
            curr = tmp 
        #print('prev here', prev.val)
        head = prev
        return head