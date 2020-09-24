def maxPathSum(tree):
    return findMPS(tree)[1]

def findMPS(tree):
	if tree is None:
		return (0, float('-inf'))

	leftMSB, leftMPS = findMPS(tree.left)
	rightMSB, rightMPS = findMPS(tree.right)
	maxChildBranch = max(leftMSB, rightMSB)

	maxSumBranch = max(maxChildBranch + tree.value, tree.value)
	maxTriangleSum = max(leftMSB + tree.value + rightMSB, maxSumBranch)
	MPS = max(maxTriangleSum, leftMPS, rightMPS)

	return (maxSumBranch, MPS)
