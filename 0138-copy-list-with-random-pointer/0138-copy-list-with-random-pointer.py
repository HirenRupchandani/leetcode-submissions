"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {None:None}

        curr=head

        while curr:
            # copy = Node(curr.val)
            # hmap[curr] = copy
            hmap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            old = hmap[curr]
            old.next = hmap[curr.next]
            old.random = hmap[curr.random]
            curr = curr.next
        return hmap[head]