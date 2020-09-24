class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
			self.setHead(nodeToInsert)
			return
		node = self.head
		currPos = 1
		while node is not None and currPos != position:
			node = node.next
			currPos += 1
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)
    def removeNodesWithValue(self, value):
        node = self.head
		while node is not None:
			toRemove = node
			node = node.next
			if toRemove.value == value:
				self.remove(toRemove)

    def remove(self, node):
        if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		self.removeLinks(node)

	def removeLinks(self, node):
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None

    def containsNodeWithValue(self, value):
        node = self.head
		while node is not None and node.value != value:
			node = node.next
		return node is not None
