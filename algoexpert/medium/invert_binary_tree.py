# Solution 1
def invertBinaryTree(tree):
    if tree is None:
		return
	swap(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

def swap(node):
	node.left, node.right = node.right, node.left

# Solution 2
def invertBinaryTree(tree):
    queue = [tree]
	while len(queue):
		current = queue.pop(0)
		if current is None:
			continue
		swap(current)
		queue.append(current.left)
		queue.append(current.right)

def swap(node):
	node.left, node.right = node.right, node.left
