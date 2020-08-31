# Solution 1
def isMonotonic(array):
    nonDecreasing = True
	nonIncreasing = True
	for i in range(1, len(array)):
		if array[i] > array[i - 1]:
			nonDecreasing = False
		if array[i] < array[i - 1]:
			nonIncreasing = False
	return nonDecreasing or nonIncreasing

# Solution 2
def isMonotonic(array):
	for num in array:
		if array.count(num) <= 1:
			return False
	return False
