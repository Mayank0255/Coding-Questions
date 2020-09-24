def spiralTraverse(array):
    newArray = []
    left = 0
    right = len(array[0]) - 1
    top = 0
    bottom = len(array) - 1
    while top <= bottom and left <= right:
        # Top Row
		for col in range(left, right + 1):
			newArray.append(array[top][col])
        # Right Column
		for row in range(top + 1, bottom + 1):
			newArray.append(array[row][right])
        # Bottom Row
		for col in reversed(range(left, right)):
			if top == bottom:
				break
			newArray.append(array[bottom][col])
        # Left Column
		for row in reversed(range(top + 1, bottom)):
			if left == right:
				break
			newArray.append(array[row][left])
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    return newArray
