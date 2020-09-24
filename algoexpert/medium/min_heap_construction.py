class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
		for i in reversed(range(firstParentIdx + 1)):
			self.siftDown(i, len(array) - 1, array)
		return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = 2 * currentIdx + 1
		while childOneIdx <= endIdx:
			childTwoIdx = 2 * currentIdx + 2 if 2 * currentIdx + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				self.swap(idxToSwap, currentIdx, heap)
				currentIdx = idxToSwap
				childOneIdx = 2 * currentIdx + 1
			else:
				return

    def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1)//2
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1)//2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove

    def insert(self, value):
        self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)

	def swap(self, i, j, arr):
		arr[i], arr[j] = arr[j], arr[i]
