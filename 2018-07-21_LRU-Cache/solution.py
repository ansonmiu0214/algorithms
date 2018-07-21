#!/bin/python3

"""
[Doubly-]linked-list ensures O(1) insertion and removal.
"""
class DoublyLinkedListNode:
	def __init__(self, key = None):
		self.key = key
		self.next = None
		self.prev = None


"""
LRU cache data structure.
Dictionary and doubly linked list supports O(1) operations.
"""
class Cache:
	def __init__(self, capacity):
		# cache count and capacity
		self.capacity = capacity
		self.count = 0

		# dictionary for key membership
		self.store = dict()

		# doubly-linked-list nodes for `old' and `new'
		self.old = DoublyLinkedListNode()
		self.new = DoublyLinkedListNode()
		self.old.next = self.new
		self.new.prev = self.old


	def get(self, key):
		if key not in self.store:
			return -1

		val, node = self.store[key]
	
		# yank node from its place in the queue
		node.prev.next = node.next
		node.next.prev = node.prev

		# place node as new tail
		self.new.prev.next = node
		node.prev = self.new.prev

		self.new.prev = node
		node.next = self.new

		return val

	def put(self, key, value):
		if key in self.store:
			# replace value
			_, node = self.store[key]
			self.store[key] = value, node

			# yank node from its place in the queue
			node.prev.next = node.next
			node.next.prev = node.prev

			# place node as new tail
			self.new.prev.next = node
			node.prev = self.new.prev

			self.new.prev = node
			node.next = self.new

		else:
			if self.count == self.capacity:
				# evict least-recently-used
				evict = self.old.next
				del self.store[evict.key]

				# remove from doubly-linked-list
				self.old.next.next.prev = self.old
				self.old.next = self.old.next.next

				self.count -= 1

			node = DoublyLinkedListNode(key)
			self.store[key] = value, node

			# place as new tail
			node.next = self.new
			node.prev = self.new.prev

			self.new.prev.next = node
			self.new.prev = node

			# increment counter
			self.count += 1


if __name__ == "__main__":
	print("Commands:")
	print("> cache [capacity]")
	print("> get [key]")
	print("> put [key] [value]")
	print("> exit")
	print()

	cache = None
	while True:
		print("> ", end="")
		cmd, *args = input().strip().split(' ')
		if cmd == "exit":
			exit(0)

		if cmd == "cache":
			capacity = int(args[0])
			cache = Cache(capacity)
			print("Cache set up with capacity {}".format(capacity))

		elif cmd == "get":
			key = int(args[0])
			val = cache.get(key)
			print("Get {} = {}".format(key, val if val != -1 else "not found"))

		elif cmd == "put":
			key, val = list(map(int, args))
			cache.put(key, val)
			print("Put mapping {}->{}".format(key, val))
