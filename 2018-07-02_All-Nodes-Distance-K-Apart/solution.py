#!/bin/python3

from collections import deque

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self): 
		return "Node {} ({}) ({})".format(self.val, str(self.left) if self.left else "", str(self.right) if self.right else "")

"""
First applies DFS to find the path from root leading to target.
Result is comprised of:
	1. target's children that are distance K from target;
	2. nodes of distance K-i from target's ith parent through paths not involving target's (i-1)th parent.
"""
def distanceK(root, target, K):
	path, _ = path_dfs(root, target)
	target = path.pop()

	nodes_forward = bfs_at_level(target, K)
	nodes_backward = backtrack(path, target, K - 1)

	return nodes_forward + nodes_backward

"""
Returns (path, found), where found is True iff node is in tree 
and path is a deque of nodes from tree leading to node.
"""
def path_dfs(tree, node):
	if node == tree:
		return deque([tree]), True

	if tree.left:
		path, found = path_dfs(tree.left, node)
		if found:
			path.appendleft(tree)
			return path, found

	if tree.right:
		path, found = path_dfs(tree.right, node)
		if found:
			path.appendleft(tree)
			return path, found

	return deque(), False

"""
Returns a list of values of nodes that reside at level K of root,
where root is level 0.
"""
def bfs_at_level(root, K):
	res = []
	stack = deque([root, 0])

	while stack:
		curr, lvl = stack.popleft()
		if lvl == K:	res.append(curr.val)	# this is part of the solution
		elif lvl > K:	return res						# lazy termination

		if curr.left:		stack.append((curr.left, lvl + 1))
		if curr.right:	stack.append((curr.right, lvl + 1))

	return res

"""
Backtrack along past nodes in path to find nodes distance K from path[-1]; recursively checks for paths not involving prev to avoid infinite loop.
"""
def backtrack(path, prev, K):
	res = []
	if not path:	return res	# cannot further backtrack
	curr = path.pop()

	if K == 0:	return [curr.val]		# part of solution
	
	# apply BFS of distance K-1 from the path not involving prev
	if curr.left and curr.left.val != prev.val:
		res += bfs_at_level(curr.left, K - 1)
	elif curr.right and curr.right.val != prev.val:
		res += bfs_at_level(curr.right, K - 1)

	# recursively backtrack for nodes with distance K-1 from next node
	# along in path not involving curr
	recursive_res = backtrack(path, curr, K - 1)

	return res + recursive_res


if __name__ == "__main__":
	print("TODO")
