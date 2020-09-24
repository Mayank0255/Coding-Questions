def productSum(array, depth = 1):
	summation = 0
	for element in array:
		if type(element) is list:
			summation += productSum(element, depth + 1)
		else:
			summation += element
	return summation * depth
