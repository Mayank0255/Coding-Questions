
# O(n) time | O(n) space - where n is length of the input string
def runLengthEncoding(string):
    encodedStrings = []
	currentRunLength = 1

	for i in range(1, len(string)):
		prevLetter = string[i - 1]
		currLetter = string[i]

		if currLetter != prevLetter or currentRunLength == 9:
			encodedStrings.append(str(currentRunLength))
			encodedStrings.append(prevLetter)
			currentRunLength = 0
		currentRunLength += 1

	encodedStrings.append(str(currentRunLength))
	encodedStrings.append(string[len(string) - 1])

	return "".join(encodedStrings)
