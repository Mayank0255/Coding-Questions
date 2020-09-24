def heapSort(array):
    buildHeap(array)
	for endIdx in reversed(range(1, len(array))):
		swap(0, endIdx, array)
		siftDown(0, endIdx - 1, array)
	return array

def buildHeap(array):
    firstParentIdx = (len(array) - 2) // 2
	for currentIdx in reversed(range(firstParentIdx + 1)):
		siftDown(currentIdx, len(array) - 1, array)

def siftDown(currentIdx, endIdx, heap):
    childOneIdx = 2 * currentIdx + 1
	while childOneIdx <= endIdx:
		childTwoIdx = 2 * currentIdx + 2 if 2 * currentIdx + 2 <= endIdx else -1
		if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
			idxToSwap = childTwoIdx
		else:
			idxToSwap = childOneIdx
		if heap[idxToSwap] > heap[currentIdx]:
			swap(idxToSwap, currentIdx, heap)
			currentIdx = idxToSwap
			childOneIdx = 2 * currentIdx + 1
		else:
			return
def swap (i, j, array):
	array[i], array[j] = array[j], array[i]
