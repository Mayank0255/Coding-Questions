def minimumWaitingTime(queries):
    queries.sort()

	currentSum = 0
	totalWaitingTime = 0
	for i in range(len(queries) - 1):
		currentSum += queries[i]
		totalWaitingTime += currentSum

    return totalWaitingTime
