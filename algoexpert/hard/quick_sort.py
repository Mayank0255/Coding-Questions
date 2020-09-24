def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
	return array

def quickSortHelper(array, startIdx, endIdx):
	if startIdx >= endIdx:
		return
	pivot = startIdx
	left = pivot + 1
	right = endIdx
	while right >= left:
		if array[left] >= array[pivot] and array[right] <= array[pivot]:
			swap(array, left, right)
		if array[left] <= array[pivot]:
			left += 1
		if array[right] >= array[pivot]:
			right -= 1
	swap(array, pivot, right)
	leftSubarrayLength = right - 1 - startIdx < endIdx - (right + 1)
	if leftSubarrayLength:
		quickSortHelper(array, startIdx, right - 1)
		quickSortHelper(array, right + 1, endIdx)
	else:
		quickSortHelper(array, right + 1, endIdx)
		quickSortHelper(array, startIdx, right - 1)

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
