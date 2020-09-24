# Solution 1
def binarySearch(array, target):
	return helper(array, target, 0, len(array) - 1)


def helper(array, target, left, right):
	if left > right:
		return -1
	middle = (left + right) // 2
	element = array[middle]
	if target == element:
		return middle
	elif target < element:
		return helper(array, target, left, middle - 1
	elif target >= element:
		return helper(array, target, middle + 1, right)

# Solution 2
def binarySearch(array, target):
    left = 0
	right = len(array) - 1
	while left <= right:
		middle = (left + right) // 2
		element = array[middle]
		if target == element:
			return middle
		elif target < element:
			right = middle - 1
		else:
			left = middle + 1
	return -1
