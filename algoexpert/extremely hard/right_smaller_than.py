def rightSmallerThan(array):
    rightSmallerCounts = []
	for i in range(len(array)):
		rightSmallerCount = 0
		for j in range(i + 1, len(array)):
			if array[j] < array[i]:
				rightSmallerCount += 1
		rightSmallerCounts.append(rightSmallerCount)
	return rightSmallerCounts
