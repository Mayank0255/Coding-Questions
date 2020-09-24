def multiStringSearch(bigString, smallStrings):
	trie = Trie()
	for string in smallStrings:
		trie.insert(string)
	containedStrings = {}
	for i in range(len(bigString)):
		findSmallStringsIn(bigString, i, trie, containedStrings)
	return [string in containedStrings for string in smallStrings]

def findSmallStringsIn(string, startIdx, trie, containedStrings):
	currentNode = trie.root
	for i in range(startIdx, len(string)):
		currentChar = string[i]
		if currentChar not in currentNode:
			break
		currentNode = currentNode[currentChar]
		if trie.endSymbol in currentNode:
			containedStrings[currentNode[trie.endSymbol]] = True

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"

	def insert(self, string):
		current = self.root
		for i in range(len(string)):
			if string[i] not in current:
				current[string[i]] = {}
			current = current[string[i]]
		current[self.endSymbol] = string
