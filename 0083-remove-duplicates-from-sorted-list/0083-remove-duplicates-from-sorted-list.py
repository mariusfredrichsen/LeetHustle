# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if not node:
            return
        
        while True:
            if node.next:
                if node.val == node.next.val:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                return head