class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
        return self

    def contains(self, value):
		if value == self.value:
			return True
		elif value < self.value:
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		else:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)
        return False

    def remove(self, value, parentNode = None):
		currentNode = self
		while currentNode is not None:
			if value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
			elif value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			else:
				if currentNode.left is not None and currentNode.right is not None:
					currentNode.value = currentNode.right.minValue()
					currentNode.right.remove(currentNode.value, currentNode)
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else:
						pass
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break
        return self

	def minValue(self):
		if self.left is None:
			return self.value
		else:
			return self.left.minValue()
