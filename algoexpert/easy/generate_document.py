# O(n + m) time | O(c) space
def generateDocument(characters, document):
    checkCharacters = {}

	for el in characters:
		if el not in checkCharacters:
			checkCharacters[el] = 0
		checkCharacters[el] += 1

	for el in document:
		if el not in checkCharacters or checkCharacters[el] == 0:
			return False
		checkCharacters[el] -= 1
    return True
