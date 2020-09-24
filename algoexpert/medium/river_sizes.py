def riverSizes(matrix):
    sizes = []
	visited = [[False for val in row] for row in matrix]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if visited[i][j]:
				continue
			traverseNode(i, j, matrix, visited, sizes)
	return sizes

def traverseNode(i, j, matrix, visited, sizes):
	currentSize = 0
	nodesToExplore = [[i, j]]
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		currentSize +=1
		unvisitedNeighbours = getNeighbours(i, j, matrix, visited)
		for neighbour in unvisitedNeighbours:
			nodesToExplore.append(neighbour)
	if currentSize > 0:
		sizes.append(currentSize)

def getNeighbours(i, j, matrix, visited):
	unvisitedNeighbours = []
	if i > 0 and not visited[i - 1][j]:
		unvisitedNeighbours.append([i - 1, j])
	if i < len(matrix) - 1 and not visited[i + 1][j]:
		unvisitedNeighbours.append([i + 1, j])
	if j > 0 and not visited[i][j - 1]:
		unvisitedNeighbours.append([i, j - 1])
	if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
		unvisitedNeighbours.append([i, j + 1])
	return unvisitedNeighbours
