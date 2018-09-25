#!/bin/python3
import sys
sys.path.append('../')

from adt import TreeNode
from collections import deque

"""
Compute parent information of both nodes first, then backtrack and return the first ancestor they share.
"""
def lowestCommonAncestor(root, p, q):
	# populate parent information
	# define dictionary mapping node value to TreeNode object of parent
	parents = { root.val: None }

	queue = deque([root])
	while queue:
		node = queue.popleft()
		if node.left:
			parents[node.left.val] = node
		
		if node.right:
			parents[node.right.val] = node

	# backtrack path to root from p
	# keep track of `seen' nodes, including p
	seen = set()
	curr = p
	while curr:
		seen.add(curr.val)
		curr = parents[curr.val]

	# backtrack path to root from q
	# first node that was seen in the previous backtrack is LCA
	res = q
	while res.val not in seen:
		res = parents[res.val]

	return res


if __name__ == "__main__":
	root = TreeNode(3)
	p = root.left = TreeNode(5)
	q = root.right = TreeNode(1)
	root.left.left = TreeNode(6)
	root.left.right = TreeNode(2)
	root.left.right.left = TreeNode(7)
	root.left.right.right = TreeNode(4)

	root.right.left = TreeNode(0)
	root.right.right = TreeNode(8)
	
	print("Tree:")
	print(root)

	print()
	print("p: {}".format(p.val))
	print("q: {}".format(q.val))

	LCA = lowestCommonAncestor(root, p, q)
	print("LCA: {}".format(LCA.val))

	
