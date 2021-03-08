# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
	currentNode = linkedList
	while currentNode is not None:
		checkNode = currentNode.next
		while checkNode is not None and checkNode.value == currentNode.value:
			checkNode = checkNode.next

		currentNode.next = checkNode
		currentNode = checkNode

    return linkedList
