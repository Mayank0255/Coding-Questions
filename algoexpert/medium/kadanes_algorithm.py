def kadanesAlgorithm(array):
    maxSoFar = array[0]
	maxEndingHere = array[0]
	for i in range(1, len(array)):
		maxEndingHere = max(array[i], maxEndingHere + array[i])
		maxSoFar = max(maxEndingHere, maxSoFar)
	return maxSoFar
