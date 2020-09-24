# Solution 1
def minHeightBst(array):
    return constructTree(array, 0, len(array) - 1)

def constructTree(array, start, end):
	if end < start:
		return

	mid = (start + end) // 2
	bst = BST(array[mid])
	bst.left = constructTree(array, start, mid - 1)
	bst.right = constructTree(array, mid + 1, end)
	return bst


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

# Solution 2
def minHeightBst(array):
    return constructTree(array, None, 0, len(array) - 1)

def constructTree(array, bst, start, end):
	if end < start:
		return

	mid = (start + end) // 2
	newBstNode = BST(array[mid])
	if bst is None:
		bst = newBstNode
	else:
		if array[mid] < bst.value:
			bst.left = newBstNode
			bst = bst.left
		else:
			bst.right = newBstNode
			bst = bst.right
	constructTree(array, bst, start, mid - 1)
	constructTree(array, bst, mid + 1, end)
	return bst


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

# Solution 3
def minHeightBst(array):
    return constructTree(array, None, 0, len(array) - 1)

def constructTree(array, bst, start, end):
	if end < start:
		return

	mid = (start + end) // 2
	valueToAdd = array[mid]
	if bst is None:
		bst = BST(valueToAdd)
	else:
		bst.insert(valueToAdd)
	constructTree(array, bst, start, mid - 1)
	constructTree(array, bst, mid + 1, end)
	return bst

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
