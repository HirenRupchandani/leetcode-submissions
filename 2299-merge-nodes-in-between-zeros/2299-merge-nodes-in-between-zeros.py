# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_val = 0
        new_head = ListNode()
        new_curr = new_head
        while curr:
            if curr.val != 0:
                new_val += curr.val
            else:
                new_node = ListNode(val = new_val)
                new_curr.next = new_node
                new_curr = new_curr.next
                new_val = 0
            curr = curr.next
        
        return new_head.next.next
        