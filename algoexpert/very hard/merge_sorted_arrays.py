def mergeSortedArrays(arrays):
    sortedList = []
	smallestItems = []
	for arrayIdx in range(len(arrays)):
		smallestItems.append({"arrayIdx": arrayIdx, "elementIdx": 0, "num": arrays[arrayIdx][0]})
	minHeap = MinHeap(smallestItems)
	while not minHeap.isEmpty():
		smallestItem = minHeap.remove()
		arrayIdx, elementIdx, num = smallestItem["arrayIdx"], smallestItem["elementIdx"], smallestItem["num"]
		sortedList.append(num)
		if elementIdx == len(arrays[arrayIdx]) - 1:
			continue
		minHeap.insert({"arrayIdx": arrayIdx, "elementIdx": elementIdx + 1, "num": arrays[arrayIdx][elementIdx + 1]})
	return sortedList


class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

	def isEmpty(self):
		return len(self.heap) == 0

    def build_heap(self, array):
        first_parent_index = (len(array) - 2) // 2
        for current_index in reversed(range(first_parent_index + 1)):
            self.sift_down(current_index, len(array) - 1, array)
        return array

    def sift_down(self, current_index, end_index, heap):
        child_one_index = current_index * 2 + 1
        while child_one_index <= end_index:
            child_two_index = current_index * 2 + 2 if current_index * 2 + 2 <= end_index else -1
            if child_two_index != -1 and heap[child_two_index]["num"] < heap[child_one_index]["num"]:
                index_to_swap = child_two_index
            else:
                index_to_swap = child_one_index
            if heap[index_to_swap]["num"] < heap[current_index]["num"]:
                self.swap(current_index, index_to_swap, heap)
                current_index = index_to_swap
                child_one_index = current_index * 2 + 1
            else:
                return

    def sift_up(self, current_index, heap):
        parent_index = (current_index - 1) // 2
        while current_index > 0 and heap[current_index]["num"] < heap[parent_index]["num"]:
            self.swap(current_index, parent_index, heap)
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    def remove(self): # We mainly remove the root node by default. the first element of the array.
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop() # Heap follows a stack data structure
        self.sift_down(0, len(self.heap) -  1, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
