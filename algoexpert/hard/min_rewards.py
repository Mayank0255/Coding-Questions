def minRewards(scores):
	root = min(scores)
    midIdx = scores.index(root)
	count = 1

	left = midIdx - 1
	right = midIdx + 1
	current = root
	giftVal = 1
	while left >= 0:
        if scores[left] < current:
            giftVal = 1
        elif scores[left] > current:
            giftVal += 1
        count += giftVal
        current = scores[left]
        left -= 1

    current = root
    giftVal = 1
    while right <= len(scores) - 1:
        if scores[right] < current:
            giftVal = 1
        elif scores[right] > current:
            giftVal += 1
        count += giftVal
        current = scores[right]
        right += 1

	return count
