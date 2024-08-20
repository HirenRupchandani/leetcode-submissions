# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)
        def dfs(root, flag):
            if not root:
                return None
            # print(root.val)
            toDel = (root.val in to_delete)
            root.left = dfs(root.left, toDel)
            root.right = dfs(root.right, toDel)
            # if the current node is not in to_delete 
            # and flag is true, then this is the root of 
            # one of the new trees and can be added to result
            if not toDel and flag:
                result.append(root)
            return None if toDel else root
        dfs(root, True)
        # print(result)
        return result


                