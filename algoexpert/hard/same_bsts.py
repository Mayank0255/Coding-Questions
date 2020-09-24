def sameBsts(arrayOne, arrayTwo):
    lengthOne = len(arrayOne)
	lengthTwo = len(arrayTwo)
	if lengthOne != lengthTwo:
		return False
	if lengthOne == 0 and lengthTwo == 0:
		return True
	if arrayOne[0] != arrayTwo[0]:
		return False

	leftOne = getLeft(arrayOne)
	leftTwo = getLeft(arrayTwo)
	rightOne = getRight(arrayOne)
	rightTwo = getRight(arrayTwo)

	return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

def getLeft(array):
	leftRes = []
	for i in range(1, len(array)):
		if array[i] < array[0]:
			leftRes.append(array[i])
	return leftRes
    
def getRight(array):
	rightRes = []
	for i in range(1, len(array)):
		if array[i] >= array[0]:
			rightRes.append(array[i])
	return rightRes
