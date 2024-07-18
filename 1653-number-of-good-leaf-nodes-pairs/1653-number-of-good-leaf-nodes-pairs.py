# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def countPairs(self, root: TreeNode, distance: int) -> int:

		res = [0] 
		def dfs(node):
			if not node:return []
			if not node.left and not node.right:return [0]
			left,right = dfs(node.left),dfs(node.right)
			m,n = len(left),len(right)
			for i in range(m):
				left[i]+=1
			for j in range(n):
				right[j]+=1

			for l in left:
				for r in right:
					if l + r <= distance:
						res[0] += 1
			return left+right
		dfs(root)
		return res[0]