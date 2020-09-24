def longestIncreasingSubsequence(array):
    sequences = [None for i in array]
	indices = [None for x in range(len(array) + 1)]
	length = 0
	for i, num in enumerate(array):
		newLength = binarySearch(1, length, indices, array, num)
		sequences[i] = indices[newLength - 1]
		indices[newLength] = i
		length = max(length, newLength)
	return buildSequence(array, sequences, indices[length])

def binarySearch(start, end, indices, array, num):
	if start > end:
		return start
	middleIdx = (start + end) // 2
	if array[indices[middleIdx]] < num:
		start = middleIdx + 1
	else:
		end = middleIdx - 1
	return binarySearch(start, end, indices, array, num)

def buildSequence(array, sequences, currentIdx):
	sequence = []
	while currentIdx is not None:
		sequence.append(array[currentIdx])
		currentIdx = sequences[currentIdx]
	return list(reversed(sequence))
	return sequence
