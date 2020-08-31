def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	smallestPair = []
	smallest = float('inf')
	current = float('inf')
	i = 0
	j = 0
	while i < len(arrayOne) and j < len(arrayTwo):
		firstNum = arrayOne[i]
		secondNum = arrayTwo[j]

		if firstNum < secondNum:
			current = secondNum - firstNum
			i += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			j += 1
		else:
			return [firstNum, secondNum]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]

	return smallestPair
