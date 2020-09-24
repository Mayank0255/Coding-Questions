def allKindsOfNodeDepths(root, depth=0):
    if root is None:
		return 0

	depthSum = (depth * (depth + 1)) / 2
	return depthSum + allKindsOfNodeDepths(root.left, depth + 1) + allKindsOfNodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
