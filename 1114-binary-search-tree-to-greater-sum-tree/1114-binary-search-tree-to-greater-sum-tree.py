# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorder(root):
            if not root:
                return
            # print(root.val)
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
        
        inorder(root)
        # print(nodes)
        n = len(nodes)
        postfix = [0 for _ in range(n)]
        postfix[0] = nodes[-1]
        for i in range(n):
            postfix[i] = postfix[i-1] + nodes[n-i-1]
        # print(postfix[::-1])
        def inorder2(root):
            if not root:
                return
            inorder2(root.left)
            root.val = postfix.pop(-1)
            # somehow pop the corresponding node
            # print(root.val)
            inorder2(root.right)
        inorder2(root)
        return root
        