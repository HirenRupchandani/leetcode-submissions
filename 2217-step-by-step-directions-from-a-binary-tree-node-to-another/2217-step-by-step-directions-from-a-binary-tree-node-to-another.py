# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], sv: int, dv: int) -> str:
        #step1 finding path from root to start element and root to end element
        self.left = []
        self.right = []
        def preorder(root,l):
            if root:
                if root.val==sv:
                    self.left = l[:]
                elif root.val==dv:
                    self.right = l[:]
                if root.left:
                    l.append('L')
                    preorder(root.left,l)
                    l.pop()
                if root.right:
                    l.append('R')
                    preorder(root.right,l)
                    l.pop()
        preorder(root,[root.val])

        #step2 finding the lowest common ancestor 
        i = 0
        while i < len(self.left) and i < len(self.right) and self.left[i] == self.right[i]:
            i += 1
        
        #marking the part of startelement to ancestor as 'U'
        #copying the part of ancestor to end element as it is
        sl = 'U' * (len(self.left) - i) if self.left else ''
        sr = ''.join(self.right[i:]) if self.right else ''
        
        return sl+sr
        

