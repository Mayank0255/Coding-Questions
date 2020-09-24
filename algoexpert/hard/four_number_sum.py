def fourNumberSum(array, targetSum):
    pairSums = {}
	result = []
	for i in range(1, len(array) - 1):
		for j in range(i + 1, len(array)):
			currentSum = array[i] + array[j]
			diff = targetSum - currentSum
			if diff in pairSums:
				for pair in pairSums[diff]:
					result.append(pair + [array[i], array[j]])

		for k in range(0, i):
			currentSum = array[i] + array[k]
			if currentSum not in pairSums:
				pairSums[currentSum] = [[array[k], array[i]]]
			else:
				pairSums[currentSum].append([array[k], array[i]])
	return result
