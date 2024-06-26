# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
        inorder(root)

        def build_tree(nodes):
            m = len(nodes) // 2
            if len(nodes) == 0:
                return 
            node = TreeNode(val = nodes[m])
            node.left = build_tree(nodes[:m])
            node.right = build_tree(nodes[m+1:]) 
            return node
        return build_tree(nodes)