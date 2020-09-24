class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDepth(topAncestor, descendantOne)
	depthTwo = getDepth(topAncestor, descendantTwo)
	if depthOne > depthTwo:
		return backTrack(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return backTrack(descendantTwo, descendantOne, depthTwo - depthOne)

def getDepth(topAncestor, descendant):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth

def backTrack(lowerDescendant, higherDescendant, diff):
	while diff > 0:
		lowerDescendant = lowerDescendant.ancestor
		diff -= 1
	while lowerDescendant != higherDescendant:
		lowerDescendant = lowerDescendant.ancestor
		higherDescendant = higherDescendant.ancestor
	return lowerDescendant
