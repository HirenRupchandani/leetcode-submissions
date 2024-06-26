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
            # return
        
        inorder(root)
        print(nodes)

        def build_tree(nodes):
            m = len(nodes) // 2
            if len(nodes) == 0:
                return 
            print(m, len(nodes))
            node = TreeNode(val = nodes[m])
            node.left = build_tree(nodes[:m])
            node.right = build_tree(nodes[m+1:]) 
            return node
        n = len(nodes) // 2
        new_root = TreeNode(val = nodes[n])
        new_root.left = build_tree(nodes[:n])
        new_root.right = build_tree(nodes[n+1:])
        return new_root



        