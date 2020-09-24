def numberOfBinaryTreeTopologies(n, cache={0: 1}):
    if n in cache:
		return cache[n]
	numberOfTrees = 0
	for leftTreeSize in range(n):
		rightTreeSize = n - 1 - leftTreeSize
		numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize, cache)
		numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize, cache)
		numberOfTrees += numberOfLeftTrees * numberOfRightTrees
	cache[n] = numberOfTrees
	return numberOfTrees
