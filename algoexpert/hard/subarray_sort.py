def subarraySort(array):
    minOutOfOrder = float('inf')
	maxOutOfOrder = float('-inf')
	for i in range(len(array)):
		if isOutOfOrder(array, i):
			minOutOfOrder = min(minOutOfOrder, array[i])
			maxOutOfOrder = max(maxOutOfOrder, array[i])
	if minOutOfOrder == float('inf'):
		return [-1, -1]

	left = 0
	while minOutOfOrder >= array[left]:
		left += 1
	right = len(array) - 1
	while maxOutOfOrder <= array[right]:
		right -= 1
	return [left, right]

def isOutOfOrder(array, i):
	if i == 0:
		return array[i] > array[i + 1]
	if i == len(array) - 1:
		return array[i] < array[i - 1]
	return array[i] > array[i + 1] or array[i] < array[i - 1]
		
