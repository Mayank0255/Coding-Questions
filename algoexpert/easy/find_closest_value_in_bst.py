# Solution 1
def findClosestValueInBst(tree, target):
    return findClosest(tree, target, tree.value)

def findClosest(tree, target, closest):
	curr = tree

	while curr is not None:
		if abs(target - curr.value) < abs(target - closest):
			closest = curr.value
		if target < curr.value:
			curr = curr.left
		elif target > curr.value:
			curr = curr.right
		else:
			break
	return closest

# Solution 2
def findClosestValueInBst(tree, target):
	return findClosest(tree, target, tree.value)

def findClosest(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - tree.value) < abs(target - closest):
		closest = tree.value
	if target < tree.value:
		return findClosest(tree.left, target, closest)
	elif target > tree.value:
		return findClosest(tree.right, target, closest)
	else:
		return closest
