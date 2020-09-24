# Solution 1
def moveElementToEnd(array, toMove):
    i = 0
	j = len(array) - 1
	while i < j:
		while i < j and array[j] == toMove:
			j -= 1
		if array[i] == toMove:
			array[i], array[j] = array[j], array[i]
		i += 1
	return array

# Solution 2
def moveElementToEnd(array, toMove):
	for num in array:
		if num == toMove:
			array.remove(toMove)
			array.append(toMove)
	return array
