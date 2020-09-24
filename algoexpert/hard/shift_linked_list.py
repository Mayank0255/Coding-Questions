def shiftLinkedList(head, k):
    listLength = 1
	listTail = head
	while listTail.next is not None:
		listTail = listTail.next
		listLength += 1

	offset = abs(k) % listLength
	if offset == 0:
		return head

	newPos = listLength - offset if k > 0 else offset
	newTail = head
	for i in range(1, newPos):
		newTail = newTail.next

	newHead = newTail.next
	newTail.next = None
	listTail.next = head
	return newHead



# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
