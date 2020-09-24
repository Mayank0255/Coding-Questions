def shiftedBinarySearch(array, target):
    return helper(array, target, 0, len(array) - 1)

def helper(array, target, left, right):
	if left > right:
		return -1
	middle = (left + right)//2
	potentialMatch = array[middle]
	leftNum = array[left]
	rightNum = array[right]
	if target == potentialMatch:
		return middle
	elif leftNum <= potentialMatch:
		if target < potentialMatch and target >= leftNum:
			return helper(array, target, left, middle - 1)
		else:
			return helper(array, target, middle + 1, right)
	else:
		if target > potentialMatch and target <= rightNum:
			return helper(array, target, middle + 1, right)
		else:
			return helper(array, target, left, middle - 1)
