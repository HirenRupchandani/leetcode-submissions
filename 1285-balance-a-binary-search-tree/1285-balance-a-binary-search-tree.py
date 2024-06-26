# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        # Use in-order traversal to get the sorted sequence of nodes
        def inorder(root):
            if not root:
                return
            # In-order sequence
            # Left
            inorder(root.left)
            # Current
            nodes.append(root.val)
            # Right
            inorder(root.right)
        inorder(root)

        # Basic logic: Looking at the sorted sequnce, we would like the median to be the root for a balanced tree
        # We can use this logic recursively for building subtrees
        def build_tree(nodes):
            # Get middle index
            m = len(nodes) // 2
            # Basic check that nodes is not empty
            if len(nodes) == 0:
                return 
            # Create a new node using the median of current nodes list
            node = TreeNode(val = nodes[m])
            # Build the left subtree by recursive call to left side of array (left of median)
            node.left = build_tree(nodes[:m])
            # Build the right subtree by recursive call to right side of array (right of median)
            node.right = build_tree(nodes[m+1:]) 
            # Return the tree
            return node
        # Final call
        return build_tree(nodes)