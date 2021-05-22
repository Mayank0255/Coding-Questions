# O(nlog(n) time | O(1) space

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort(reverse=fastest)
	total = 0

	for i in reversed(range(len(redShirtSpeeds))):
		total += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return total
