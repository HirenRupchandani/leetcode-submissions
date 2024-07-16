# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        visited = []
        kids = set()
        tree = {}
        for root, child, isleft in descriptions:
            # print(root)
            kids.add(child)
            parent = tree.setdefault(root, TreeNode(root))
            kid = tree.setdefault(child, TreeNode(child))
            if isleft == 1:
                parent.left = kid
            else:
                parent.right = kid
        return tree[(tree.keys() - kids).pop()]