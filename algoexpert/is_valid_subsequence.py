# Solution 1
def isValidSubsequence(array, sequence):
    seqIndx = 0

	for num in array:
		if seqIndx == len(sequence):
			break
		if num == sequence[seqIndx]:
			seqIndx += 1
	return seqIndx == len(sequence)

# Solution 2
def isValidSubsequence(array, sequence):
    arrIndx = 0
	seqIndx = 0

	while seqIndx < len(sequence) and arrIndx < len(array):
		if array[arrIndx] == sequence[seqIndx]:
			seqIndx += 1
		arrIndx += 1

	return seqIndx == len(sequence)
