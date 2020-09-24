def squareOfZeroes(matrix):
	n = len(matrix)
	for topRow in range(n):
		for leftCol in range(n):
			squareLength = 2
			while squareLength <= n - leftCol and squareLength <= n - topRow:
				bottomRow = topRow + squareLength - 1
				rightCol = leftCol + squareLength - 1
				if isSquareOfZeroes(matrix, topRow, leftCol, bottomRow, rightCol):
					return True
				squareLength += 1
	return False

def isSquareOfZeroes(matrix, r1, c1, r2, c2):
	for row in range(r1, r2 + 1):
		if matrix[row][c1] != 0 or matrix[row][c2] != 0:
			return False
	for col in range(c1, c2 + 1):
		if matrix[r1][col] != 0 or matrix[r2][col] != 0:
			return False
	return True

	
