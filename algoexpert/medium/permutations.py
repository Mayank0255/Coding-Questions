def getPermutations(array):
    permutations = []
	permutationsHelper(array, [], permutations)
	return permutations

def permutationsHelper(array, current, permutations):
	if not len(array) and len(current):
		permutations.append(current)
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i + 1:]
			newCurrent = current + [array[i]]
			permutationsHelper(newArray, newCurrent, permutations)
