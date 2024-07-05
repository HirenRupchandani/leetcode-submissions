# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # keep track of node-count, critical points
        cp = []
        # index of critical point, and previous node value
        index = 0
        prev = head.val
        
        result = [-1, -1]

        while head.next:
            # Tests for critical points: product < 0 if and only if
            #          prev < head.val > head.next.val, or 
            #          prev > head.val < head.next.val
            if (prev-head.val)*(head.val-head.next.val) < 0:
                cp.append(index)
            
            # iterates to next node and increments node-count
            prev, head = head.val, head.next
            index += 1
        
        n = len(cp)

        # fewer than 2 nodes
        if n<2:
            return [-1, -1]
        # list already sorted, so min is least dist between consecutive elements;
        mini = min((cp[i] - cp[i-1] for i in range(1,n)))

        # max is last element - 1st element
        maxi = cp[-1] - cp[0]

        return [mini, maxi]
