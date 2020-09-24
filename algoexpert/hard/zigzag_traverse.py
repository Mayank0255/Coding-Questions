def zigzagTraverse(array):
    width = len(array[0]) - 1
	height = len(array) - 1
	result = []
	row, col = 0, 0
	goingDown = True
	while not isOutOfBounds(row, col, height, width):
		result.append(array[row][col])
		if goingDown:
			if col == 0 or row == height:
				goingDown = False
				if row == height:
					col += 1
				else:
					row += 1
			else:
				col -= 1
				row += 1
		else:
			if col == width or row == 0:
				goingDown = True
				if col == width:
					row += 1
				else:
					col += 1
			else:
				row -= 1
				col += 1
	return result

def isOutOfBounds(row, col, height, width):
	return row < 0 or col < 0 or row > height or col > width
