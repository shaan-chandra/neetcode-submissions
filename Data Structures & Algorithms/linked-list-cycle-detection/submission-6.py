# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # o(n) sol and memory is have a set 
        hashset = set()
        curr = head
        while curr:
            if curr in hashset:
                return True
            hashset.add(curr)
            curr = curr.next
        return False