def hasSingleCycle(array):
	nums = 0
    currIdx = 0
	while nums < len(array):
		if nums > 0 and currIdx == 0:
			return False
		nums += 1
		currIdx = getNextIdx(currIdx, array)
	return currIdx == 0


def getNextIdx(currentIndex, array):
	jump = array[currentIndex]
	nextIndex = (currentIndex + jump) % len(array)
	return nextIndex if nextIndex >= 0 else nextIndex + len(array)
