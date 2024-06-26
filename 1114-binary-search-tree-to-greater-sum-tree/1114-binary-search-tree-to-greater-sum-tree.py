# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodes = []
        # Normal inorder to get the sequence of nodes in ascending
        self.total = 0
        def inorder(root):
            if not root:
                return
            # print(root.val)
            inorder(root.right)
            self.total += root.val
            # nodes.append(root.val)
            root.val = self.total
            inorder(root.left)
        
        inorder(root)
        # print(nodes)
        # n = len(nodes)

        # # Let's create a postfix sum array using the sequence
        # postfix = [0 for _ in range(n)]
        # postfix[0] = nodes[-1]
        # for i in range(n):
        #     postfix[i] = postfix[i-1] + nodes[n-i-1]
        # # print(postfix[::-1])

        # # Using another inorder traversal, keep replacing the node value with postfix sum
        # def inorder2(root):
        #     if not root:
        #         return
        #     inorder2(root.left)
        #     root.val = postfix.pop(-1)
        #     # pop the corresponding node which is at the end
        #     # print(root.val)
        #     inorder2(root.right)
        # inorder2(root)
        return root
        