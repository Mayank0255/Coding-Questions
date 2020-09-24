def selectionSort(array):
    currIdx = 0
	while currIdx < len(array) - 1:
		smallIdx = currIdx
		for i in range(currIdx + 1, len(array)):
			if array[smallIdx] > array[i]:
				smallIdx = i
		array[currIdx], array[smallIdx] = array[smallIdx], array[currIdx]
		currIdx += 1
	return array
