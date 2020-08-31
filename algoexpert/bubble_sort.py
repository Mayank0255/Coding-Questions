def bubbleSort(array):
	n = len(array)
	i = 0
	isSorted = False
	while not isSorted:
		j = 0
		isSorted = True
		while j < n - i - 1:
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				isSorted = False
			j += 1
		i += 1
	return array
