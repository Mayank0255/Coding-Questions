# Solution 1
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums

def calculateBranchSums(root, currentSum, sums):
	if root is None:
		return

	currentSum += root.value
	if root.left is None and root.right is None:
		sums.append(currentSum)

	calculateBranchSums(root.left, currentSum, sums)
	calculateBranchSums(root.right, currentSum, sums)
