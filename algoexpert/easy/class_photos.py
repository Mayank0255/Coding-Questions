def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)

    check = 'red' if redShirtHeights[0] > blueShirtHeights[0] else 'blue'
	for i in range(len(redShirtHeights)):
		redShirtHeight = redShirtHeights[i]
		blueShirtHeight = blueShirtHeights[i]

		if check == 'red' and redShirtHeight <= blueShirtHeight:
			return False
		elif check == 'blue' and redShirtHeight >= blueShirtHeight:
			return False

    return True
    

# Not correct but if shuffling is not allowed then this is correct
# O(n) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
	check = 'red' if max(redShirtHeights) > max(blueShirtHeights) else 'blue'

	for i in range(len(redShirtHeights)):
		if check == 'red' and redShirtHeights[i] <= blueShirtHeights[i]:
			return False
		elif check == 'blue' and redShirtHeights[i] >= blueShirtHeights[i]:
			return False

    return True
