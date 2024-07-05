# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cp = []
        index = 0
        prev = head.val
        
        result = [-1, -1]

        while head.next:
            if (prev-head.val)*(head.val-head.next.val) < 0:
                cp.append(index)
            prev, head = head.val, head.next
            index += 1
        
        n = len(cp)
        if n<2:
            return [-1, -1]
        mini = min((cp[i] - cp[i-1] for i in range(1,n)))
        maxi = cp[-1] - cp[0]

        return [mini, maxi]
