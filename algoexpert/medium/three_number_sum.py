# Solution 1
def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    length = len(array)
    for i in range(length - 2):
        left = i + 1
        right = length - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum > targetSum:
                right -= 1
            elif currentSum < targetSum:
                left += 1
    return result

# Solution 2
def threeNumberSum(array, targetSum):
	result = []
	length = len(array)

	i = 0
	while i < length:
		j = i
		potentialMatch = targetSum - array[i]
		while j < length:
			potentialMatch -= array[j]
			if potentialMatch in array[j+1:]:
				res = [array[i], array[j], potentialMatch]
				result.append(sorted(res))
			j += 1
		i += 1

    return sorted(result)
