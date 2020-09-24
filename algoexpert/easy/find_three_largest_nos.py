def findThreeLargestNumbers(array):
	largest = [ array[0], array[1], array[2] ]
	largest.sort()
	for num in range(3, len(array)):
		if array[num] >= largest[0]:
			if array[num] >= largest[1]:
				if array[num] >= largest[2]:
					largest[0] = largest[1]
					largest[1] = largest[2]
					largest[2] = array[num]
				else:
					largest[0] = largest[1]
					largest[1] = array[num]
			else:
				largest[0] = array[num]
	return largest
